import logging
import os
import sys
from datetime import timedelta
from logging.handlers import RotatingFileHandler

import openai
from dotenv import dotenv_values, load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended.exceptions import (InvalidHeaderError, JWTDecodeError,
                                           NoAuthorizationError)

from .extensions import bcrypt, db, jwt, migrate


def create_app(*args, **kwargs):
    from . import routes
    from .models import SavedPlan, User  # Local import
    from .routes import main_blueprint

    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "*"}})

    try:
        # Check if the app is running on Heroku
        if 'DYNO' in os.environ:
            if not os.environ.get("DATABASE_URL"):
                raise ValueError("Missing DATABASE_URL environment variable")
            
            # Heroku
            openai.api_key = os.environ.get("OPENAI_API_KEY")
            
            database_url = os.environ.get("DATABASE_URL")
            if database_url.startswith("postgres://"):
                database_url = database_url.replace("postgres://", "postgresql://", 1)
            app.logger.info(f"Modified DATABASE_URL: {database_url}")
            app.config['SQLALCHEMY_DATABASE_URI'] = database_url
            
            app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
            app.logger.info("Running on Heroku")
        else:
            # Local Env
            load_dotenv(".env")
            config = dotenv_values(".env")
            openai.api_key = config["OPENAI_API_KEY"]
            app.config['SQLALCHEMY_DATABASE_URI'] = config["SQLALCHEMY_DATABASE_URI"]
            app.config['JWT_SECRET_KEY'] = config['JWT_SECRET_KEY']
            app.logger.info("Running locally")

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(weeks=1)

        # Set up logging
        if not app.debug:
            if 'DYNO' in os.environ:
                # Logging to stdout on Heroku
                stream_handler = logging.StreamHandler(sys.stdout)
                stream_handler.setFormatter(logging.Formatter(
                    '%(asctime)s %(levelname)s: %(message)s '
                    '[in %(pathname)s:%(lineno)d]'))
                stream_handler.setLevel(logging.INFO)
                app.logger.addHandler(stream_handler)
                app.logger.info('Logging to stdout on Heroku')
            else:
                # Logging to a file when not on Heroku
                if not os.path.exists('logs'):
                    os.mkdir('logs')
                file_handler = RotatingFileHandler('logs/gpt-fitness.log', maxBytes=10240,
                                                   backupCount=10)
                file_handler.setFormatter(logging.Formatter(
                    '%(asctime)s %(levelname)s: %(message)s '
                    '[in %(pathname)s:%(lineno)d]'))
                file_handler.setLevel(logging.INFO)
                app.logger.addHandler(file_handler)
                app.logger.info('Logging to a file')
            
            app.logger.setLevel(logging.INFO)
            app.logger.info('GPT-Fitness startup')

        # Additional Logging Statements
        app.logger.info('Before initializing Database, JWT, Bcrypt, and Migrate')
        # Initialize Database, JWT, Bcrypt, and Migrate
        db.init_app(app)
        jwt.init_app(app)
        bcrypt.init_app(app)
        migrate.init_app(app, db)
        app.logger.info('Database, JWT, Bcrypt, and Migrate initialized successfully')
        
        # Import and Register Blueprints
        app.logger.info('Before registering blueprints')
        app.register_blueprint(main_blueprint)
        app.logger.info('Blueprints registered successfully')

        @app.errorhandler(NoAuthorizationError)
        def handle_auth_error(e):
            return jsonify(error=str(e)), 401

        @app.errorhandler(InvalidHeaderError)
        def handle_invalid_header_error(e):
            return jsonify(error=str(e)), 400

        @app.errorhandler(JWTDecodeError)
        def handle_jwt_decode_error(e):
            return jsonify(error=str(e)), 400

        @app.errorhandler(Exception)
        def handle_generic_error(e):
            app.logger.error(f"Unhandled Exception: {e}", exc_info=True)
            return jsonify(error=str(e)), 500

    except Exception as e:
        app.logger.error(f"Error during app initialization: {e}", exc_info=True)
        raise
    
    app.logger.info('Flask app created successfully!')

    return app
