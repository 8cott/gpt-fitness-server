from flask import Flask, jsonify, request
import openai
from dotenv import dotenv_values, load_dotenv
from .extensions import db, jwt, bcrypt, migrate
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError, JWTDecodeError
from flask_cors import CORS
from datetime import timedelta
import logging
from logging.handlers import RotatingFileHandler
import os

logging.basicConfig(level=logging.DEBUG)

def create_app(*args, **kwargs):
    request_logger = logging.getLogger('request_logger')
    request_logger.setLevel(logging.INFO)
    request_handler = logging.StreamHandler()
    request_handler.setLevel(logging.INFO)
    request_formatter = logging.Formatter('%(asctime)s - %(message)s')
    request_handler.setFormatter(request_formatter)
    request_logger.addHandler(request_handler)

    logging.debug("Before Flask app instantiation")
    app = Flask(__name__)
    logging.debug("After Flask app instantiation")

    CORS(app, resources={r"/*": {"origins": "*"}})

    # Check if the app is running on Heroku
    if 'DYNO' in os.environ:
        if not os.environ.get("DATABASE_URL"):
            raise ValueError("Missing DATABASE_URL environment variable")
        
        # Heroku
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        
        database_url = os.environ.get("DATABASE_URL")
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
        
        app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    else:
        # Local Env
        load_dotenv(".env")
        config = dotenv_values(".env")
        openai.api_key = config["OPENAI_API_KEY"]
        app.config['SQLALCHEMY_DATABASE_URI'] = config["SQLALCHEMY_DATABASE_URI"]
        app.config['JWT_SECRET_KEY'] = config['JWT_SECRET_KEY']

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(weeks=1)

    # Initialize Database, JWT, Bcrypt, and Migrate
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Import Models
    from .models import User, SavedPlan

    # Import Routes
    from . import routes

    # Import and Register Blueprints (we will create these next)
    from .routes import main_blueprint
    app.register_blueprint(main_blueprint)

    @app.errorhandler(NoAuthorizationError)
    def handle_auth_error(e):
        return jsonify(error=str(e)), 401

    @app.errorhandler(InvalidHeaderError)
    def handle_invalid_header_error(e):
        return jsonify(error=str(e)), 400

    @app.errorhandler(JWTDecodeError)
    def handle_jwt_decode_error(e):
        return jsonify(error=str(e)), 400

    # Set up logging
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/gpt-fitness.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('GPT-Fitness startup')

    return app