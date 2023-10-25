import os
import sys
from datetime import timedelta
import openai
from dotenv import dotenv_values, load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended.exceptions import (InvalidHeaderError, JWTDecodeError,
                                           NoAuthorizationError)

from .extensions import bcrypt, db, jwt, migrate
from app import models


def create_app(*args, **kwargs):
    from . import routes
    from .models import SavedFitnessPlan, SavedDietPlan, User
    from .routes import main_blueprint

    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "*"}})

    try:
        # Check if the app is running on Heroku
        if 'DYNO' in os.environ:
            print("Running on Heroku - 'DYNO' environment variable detected")
            if not os.environ.get("DATABASE_URL"):
                raise ValueError("Missing DATABASE_URL environment variable")

            # Heroku
            openai.api_key = os.environ.get("OPENAI_API_KEY")

            database_url = os.environ.get("DATABASE_URL")
            if database_url.startswith("postgres://"):
                database_url = database_url.replace(
                    "postgres://", "postgresql://", 1)
            app.config['SQLALCHEMY_DATABASE_URI'] = database_url

            app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
        else:
            # Local Env
            print("Running locally - 'DYNO' environment variable not detected")
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

        # Import and Register Blueprints
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

        @app.errorhandler(Exception)
        def handle_generic_error(e):
            return jsonify(error=str(e)), 500

    except Exception as e:
        raise

    return app
