from flask import Blueprint, request, jsonify
from .extensions import db
from .models import User, SavedPlan
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import openai
import openai.error
from datetime import datetime


def error_response(status_code, message):
    response = {
        "success": False,
        "error": {
            "code": status_code,
            "message": message
        }
    }
    return jsonify(response), status_code


main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/generate_plan", methods=["POST"])
def generate_plan():

    try:
        data = request.get_json()

        required_keys = ["user_id", "age", "weight", "feet",
                         "inches", "goals", "days_per_week", "dietary_restrictions"]
        if not all(key in data for key in required_keys):
            return error_response(400, "Missing fields!")

        user_id = data["user_id"]
        age = data["age"]
        weight = data["weight"]
        feet = data["feet"]
        inches = data["inches"]
        goals = data["goals"]
        days_per_week = data["days_per_week"]
        dietary_restrictions = data["dietary_restrictions"]

        # PROMPT for gpt-3.5-turbo
        prompt = (f"I need a fitness plan and diet plan for someone who is {age} years old, weighs {weight} lbs, "
                  f"is {feet} feet {inches} inches tall, and wants to workout {days_per_week} days a week "
                  f"with the goal of '{goals}'. Please do not include an active rest day or any rest day. Please provide:\n\n"
                  "1. Workout Routine\n"
                  f"Please provide a workout routine for {days_per_week} \n"
                  "2. Workout Summary\n"
                  f"Please provide a summary explaining why this workout was chosen. It should not be more than a paragraph long.\n"
                  "3. Three-Day Diet Plan:\n"
                  f"Please provide a diet plan for 3 days. Unless 'None' is chosen, please include foods that are part of the following diet: {dietary_restrictions}\n"
                  "   - Day 1: Breakfast, Lunch, Dinner, Snack\n"
                  "   - Day 2: Breakfast, Lunch, Dinner, Snack\n"
                  "   - Day 3: Breakfast, Lunch, Dinner, Snack\n"
                  "4. Diet Plan Summary\n"
                  f"Please provide a summary explaining why this diet plan was chosen. It should not be more than a paragraph long.\n")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a fitness assistant."},
                      {"role": "user", "content": prompt}]
        )

        plan = response.choices[0].message["content"]

        return jsonify({"user_id": user_id, "plan": plan})

    # OpenAI Error Handling:
    except openai.error.RateLimitError:
        return error_response(429, "Rate limit exceeded, please try again later.")

    except openai.error.AuthenticationError:
        return error_response(401, "OpenAI authentication failed. Please check your API key.")

    except openai.error.InvalidRequestError as e:
        return error_response(400, f"Invalid request to OpenAI: {str(e)}")

    except openai.error.OpenAIError as e:
        return error_response(500, f"OpenAI Error: {str(e)}")

    except Exception as e:  # General catch-all for other errors
        return error_response(500, str(e))

# Validate Password
def is_valid_password(password):
    # Ensure password has at least 8 characters
    if len(password) < 8:
        return False
    # Ensure password has at least one uppercase, one lowercase, and one digit
    if not (any(char.isdigit() for char in password) and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password)):
        return False
    return True

# Users POST Route
@main_blueprint.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Check for missing fields
    if not all([username, email, password]):
        return error_response(400, "Missing Fields!")

    # Validate the password
    if not is_valid_password(password):
        return error_response(400, "Password must be at least 8 characters long, contain an uppercase letter, a lowercase letter, and a digit")

    # Check if the username or email already exists
    if User.query.filter_by(username=username).first():
        return error_response(400, "Username already exists!")
    if User.query.filter_by(email=email).first():
        return error_response(400, "Email already exists!")

    new_user = User(
        username=data["username"],
        email=data["email"],
        age=data.get("age"),
        weight=data.get("weight"),
        feet=data.get("feet"),
        inches=data.get("inches"),
        goals=data.get("goals"),
        days_per_week=data.get("days_per_week"),
        dietary_restrictions=data.get("dietary_restrictions")
    )
    new_user.set_password(data["password"])

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully!"}), 201


# Get User Route
@main_blueprint.route("/users/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "age": user.age,
        "weight": user.weight,
        "feet": user.feet,
        "inches": user.inches,
        "goals": user.goals,
        "days_per_week": user.days_per_week,
        "dietary_restrictions": user.dietary_restrictions,
    })

# Update User Route
@main_blueprint.route("/users/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    # Get the authenticated user's ID from the JWT token and ensure it's an integer
    authenticated_user_id = int(get_jwt_identity())

    # Ensure that the authenticated user is updating their own profile
    if user_id != authenticated_user_id:
        return error_response(403, "Unauthorized action!")

    user = User.query.get_or_404(user_id)
    data = request.get_json()

    # Check if the old_password and new password fields are present
    if "old_password" in data and "new_password" in data:
        # Check the old password
        if not user.check_password(data["old_password"]):
            return error_response(400, "Current password is incorrect")

        # Validate the new password
        if not is_valid_password(data["new_password"]):
            return error_response(400, "Password must be at least 8 characters long, contain an uppercase letter, a lowercase letter, and a digit")

        # If validation passes, update the password
        user.set_password(data["new_password"])

    # Validate if the new username or email is not already taken by another user
    new_username = data.get("username")
    if new_username and new_username != user.username:
        existing_user = User.query.filter_by(username=new_username).first()
        if existing_user:
            return error_response(400, "Username already exists!")

    new_email = data.get("email")
    if new_email and new_email != user.email:
        existing_user = User.query.filter_by(email=new_email).first()
        if existing_user:
            return error_response(400, "Email already exists!")

    # If validation passes, update the other fields
    if new_username:
        user.username = new_username
    if new_email:
        user.email = new_email

    user.age = data.get("age", user.age)
    user.weight = data.get("weight", user.weight)
    user.feet = data.get("feet", user.feet)
    user.inches = data.get("inches", user.inches)
    user.goals = data.get("goals", user.goals)
    user.days_per_week = data.get("days_per_week", user.days_per_week)
    user.dietary_restrictions = data.get(
        "dietary_restrictions", user.dietary_restrictions)

    db.session.commit()
    return jsonify({"message": "User updated successfully!"})


# Users DELETE Route
@main_blueprint.route("/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    authenticated_user_id = int(get_jwt_identity())
    if user_id != authenticated_user_id:
        return error_response(403, "Unauthorized action!")

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully!"})

# Users LOGIN Route
@main_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    # Check for missing fields
    if not all([username, password]):
        return error_response(400, "Missing fields!")
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return error_response(401, "Invalid username or password")

# Save Plan POST Route
@main_blueprint.route("/save_plan", methods=["POST"])
@jwt_required()
def save_plan():
    try:
        # Get data from request
        data = request.get_json()
        user_id = data["user_id"]
        plan = data["plan"]

        # Create a new SavedPlan object
        new_plan = SavedPlan(
            user_id=user_id,
            plan=plan
        )

        db.session.add(new_plan)
        db.session.commit()

        return jsonify({"message": "Plan saved successfully!"}), 201

    except Exception as e:
        return error_response(500, str(e))

# Users GET Route
@main_blueprint.route("/my_plans", methods=["GET"])
@jwt_required()
def get_user_plans():
    try:
        # Fetch the user id from the JWT
        user_id = get_jwt_identity()

        # Fetch all plans for the user that are not soft-deleted
        plans = SavedPlan.query.filter_by(
            user_id=user_id).all()

        # Serialize the plans for JSON response
        plans_list = [{
            'id': plan.id,
            'plan': plan.plan,
            'created_at': plan.created_at.strftime('%Y-%m-%d %H:%M:%S')
        } for plan in plans]

        return jsonify(plans_list)

    except Exception as e:
        return error_response(500, str(e))
