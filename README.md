# GPT Fitness - Server Side
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/Flask-2.0%2B-blue.svg)](https://flask.palletsprojects.com/)
[![Flask-JWT-Extended](https://img.shields.io/badge/Flask--JWT--Extended-4.5.2-blue)](https://flask-jwt-extended.readthedocs.io/en/stable/)
[![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-3.1.1-blue)](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
[![Flask-Bcrypt](https://img.shields.io/badge/Flask--Bcrypt-1.0.1-blue)](https://pypi.org/project/Flask-Bcrypt/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-21.2.0-blue)](https://gunicorn.org/)

This is the server-side of the GPT Fitness app. This app allows user from the client side to input their physical stats, workout days per week, and dietary restrictions and submit a request to the gpt-3.5-turbo api from openai, which will send back a custom fitness and diet plan. Users who signup and login have the ability to save their plans and delete them. Whenever a logged in user clicks the submit button, their details are saved so they do not need to keep entering them again.
Future updates will include the ability to print and email plans.

The server is built using Python 3, Flask, and Postgresql.

## Live Demo
Check out the live demo of the Real Estate Listings App [here](https://gpt-fitness-chi.vercel.app/).

## Table of Contents
- [Technologies Used](#technologies-used)
- [Setup & Installation](#installation)
- [Deployment](#deployment)
- [API Endpoints](#api-endpoints)
- [License](#license)
- [Contact Information](#contact-information)

## Technologies Used

- **Backend:**
  - [OpenAI API](https://beta.openai.com/docs/): Utilized to generate custom diet and fitness plans using GPT-3.5 Turbo.
  - [Flask](https://flask.palletsprojects.com/): A lightweight web framework for building the backend of the application.
  - [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/): Flask extension for JSON Web Tokens (JWT) authentication.
  - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/): Integration of SQLAlchemy with Flask for database management.
  - [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/): Flask extension for password hashing.
  - [Flask-Migrate](https://flask-migrate.readthedocs.io/): Flask extension for database migrations.
  
- **Frontend:**
  - [React](https://reactjs.org/): A JavaScript library for building the user interface.
  - [Vite](https://vitejs.dev/): A fast build tool and development server for frontend projects.
  
- **Database:**
  - [PostgreSQL](https://www.postgresql.org/): A powerful, open-source relational database system.

- **Deployment:**
  - [Heroku](https://www.heroku.com/): A cloud platform used for hosting the application.

- **Version Control:**
  - [Git](https://git-scm.com/): Distributed version control system used for managing project source code.

- **Package Management:**
  - [pip](https://pip.pypa.io/en/stable/): Python package manager for installing project dependencies.
  
- **Other Tools:**
  - [dotenv](https://pypi.org/project/python-dotenv/): Used for loading environment variables from a `.env` file.
  - [axios](https://axios-http.com/): A promise-based HTTP client for making API requests in React.
  - [Flask-Cors](https://flask-cors.readthedocs.io/): Flask extension for handling Cross-Origin Resource Sharing (CORS).

## Setup and Installation

To set up and run the GPT Fitness application, follow these steps:

1. **Clone the Repository:**
   git clone <https://github.com/8cott/gpt-fitness-server.git>
   cd gpt-fitness

2. **Create a Virtual Environment (Optional but Recommended):**
python -m venv venv
source venv/bin/activate

3. **Install Dependencies:**
pip install -r requirements.txt

4. **Set Environment Variables:**
Create a .env file in the project root and add the following environment variables:
OPENAI_API_KEY=your_openai_api_key
SQLALCHEMY_DATABASE_URI=your_database_uri
JWT_SECRET_KEY=your_jwt_secret_key

5. **Initialize the Database:**
flask db init
flask db migrate
flask db upgrade

6. **Run the Application**
python3 run.py

## API Endpoints

The GPT Fitness application provides the following API endpoints for interacting with the backend:

1. **Generate Custom Plan (POST):**
   - Endpoint: `/generate_plan`
   - Method: POST
   - Description: Generate a custom diet and fitness plan based on user inputs.
   - Authentication: Not required.
   
2. **Save Plan (POST, JWT protected):**
   - Endpoint: `/save_plan`
   - Method: POST
   - Description: Save a generated plan for a user.
   - Authentication: Requires JWT token.
   
3. **Get User's Saved Plans (GET, JWT protected):**
   - Endpoint: `/my_plans`
   - Method: GET
   - Description: Retrieve all saved plans for the authenticated user.
   - Authentication: Requires JWT token.
   
4. **Get Specific Saved Plan (GET, JWT protected):**
   - Endpoint: `/my_plans/{plan_id}`
   - Method: GET
   - Description: Retrieve a specific saved plan by its ID for the authenticated user.
   - Authentication: Requires JWT token.
   
5. **Delete Saved Plan (DELETE, JWT protected):**
   - Endpoint: `/my_plans/{plan_id}`
   - Method: DELETE
   - Description: Delete a specific saved plan by its ID for the authenticated user.
   - Authentication: Requires JWT token.
   
6. **Create User Account (POST):**
   - Endpoint: `/users`
   - Method: POST
   - Description: Create a new user account.
   - Authentication: Not required.
   
7. **Get User Details (GET, JWT protected):**
   - Endpoint: `/users/{user_id}`
   - Method: GET
   - Description: Retrieve user details by user ID.
   - Authentication: Requires JWT token.
   
8. **Update User Details (PUT, JWT protected):**
   - Endpoint: `/users/{user_id}`
   - Method: PUT
   - Description: Update user details by user ID.
   - Authentication: Requires JWT token.
   
9. **Delete User Account (DELETE, JWT protected):**
   - Endpoint: `/users/{user_id}`
   - Method: DELETE
   - Description: Delete a user account by user ID.
   - Authentication: Requires JWT token.
   
10. **User Login (POST):**
    - Endpoint: `/login`
    - Method: POST
    - Description: User login to obtain an access token.
    - Authentication: Not required.

Each endpoint serves a specific purpose within the application, and the documentation in the code (`app/routes.py`) provides more details on their functionality and usage.

Feel free to customize this section as needed and add any additional information or explanations for each endpoint.

## Deployment
The client side of this app is deployed on [Heroku](https://gpt-fitness-server-5c53c1ab4ccd.herokuapp.com/)

## License
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the ISC License. See the [LICENSE](LICENSE) file for details.

## Contact Information
For any questions or feedback, please feel free to reach out to me:
- Scott Rubin
- Email: scottrubin@gmail.com