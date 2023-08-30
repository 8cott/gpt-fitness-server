# gpt-fitness/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openai
from dotenv import dotenv_values

# Initialize Flask app
app = Flask(__name__)

# Debug Mode
app.debug = True

# Load environment variables
config = dotenv_values(".env")

# Set up OpenAI
openai.api_key = config["OPENAI_API_KEY"]

# Flask SQLAlchemy Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = config["SQLALCHEMY_DATABASE_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Import routes
from . import routes
