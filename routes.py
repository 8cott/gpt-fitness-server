from . import app, db
from .models import User, SavedPlan
from flask import request, jsonify
import openai

# Generate Fitness/Diet Plan Route
@app.route("/generate_plan", methods=["POST"])
def generate_plan():
    try:
        # Get user data from request
        data = request.get_json()
        user_id = data["user_id"]
        age = data["age"]
        weight = data["weight"]
        feet = data["feet"]
        inches = data["inches"]
        goals = data["goals"]
        days_per_week = data["days_per_week"]
        dietary_restrictions = data["dietary_restrictions"]

        # Construct the prompt
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

    except Exception as e:
        return jsonify({"error": str(e)})

# Users POST Route
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
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


# GET all Users Route
@app.route("/users", methods=["GET"])
def get_all_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
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
        }
        user_list.append(user_data)
    return jsonify(user_list)


# Get 1 User Route
@app.route("/users/<int:user_id>", methods=["GET"])
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

# Users PUT Route
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    user.age = data.get("age", user.age)
    user.weight = data.get("weight", user.weight)
    user.feet = data.get("feet", user.feet)
    user.inches = data.get("inches", user.inches)
    user.goals = data.get("goals", user.goals)
    user.days_per_week = data.get("days_per_week", user.days_per_week)
    user.dietary_restrictions = data.get("dietary_restrictions", user.dietary_restrictions)
    if "password" in data:
        user.set_password(data["password"])
    db.session.commit()
    return jsonify({"message": "User updated successfully!"})

# Users DELETE Route
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully!"})

# Save Plan POST Route
@app.route("/save_plan", methods=["POST"])
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
        return jsonify({"error": str(e)})
