from flask import Flask, request, jsonify
import openai
from dotenv import dotenv_values

app = Flask(__name__)

# Configure OpenAI API KEY
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

@app.route("/generate_plan", methods=["POST"])
def generate_plan():
    try:
        # Get user data from request
        data = request.get_json()
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

        plan = response.choices[0].message['content']

        # Split the plan into its constituent parts
        sections = plan.split("\n\n")

        # Extract each section and map it to the relevant key
        structured_plan = {
            "workout_routine": sections[0],
            "workout_summary": sections[1],
            "diet_plan": "\n\n".join(sections[2:5]),
            "diet_summary": sections[5]
        }

        return jsonify({"plan": plan})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)