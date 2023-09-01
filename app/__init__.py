from flask import Flask, jsonify
import openai
from dotenv import dotenv_values
from .extensions import db, jwt, bcrypt, migrate
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError, JWTDecodeError


def create_app():
    app = Flask(__name__)

    # Load environment variables
    config = dotenv_values(".env")

    # Set up OpenAI
    openai.api_key = config["OPENAI_API_KEY"]

    # Flask SQLAlchemy Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = config["SQLALCHEMY_DATABASE_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Set JWT Secret Key
    app.config['JWT_SECRET_KEY'] = config['JWT_SECRET_KEY']

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

    return app
