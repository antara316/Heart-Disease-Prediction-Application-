from flask_login import UserMixin
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB using URI from environment variables
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.heart_disease_db  # Access the specific database

# User model for authentication and user-related operations
class User(UserMixin):
    def __init__(self, user_data):
        # Initialize user object with necessary attributes
        self.id = str(user_data['_id'])
        self.name = user_data['name']
        self.email = user_data['email']
        self.password = user_data['password']

    @staticmethod
    def get_by_id(user_id):
        # Fetch user from database using user ID
        user_data = db.users.find_one({'_id': ObjectId(user_id)})
        if user_data:
            return User(user_data)
        return None

    @staticmethod
    def get_by_email(email):
        # Fetch user from database using email
        user_data = db.users.find_one({'email': email})
        if user_data:
            return User(user_data)
        return None

    @staticmethod
    def create(name, email, password):
        # Create a new user in the database
        user_data = {
            'name': name,
            'email': email,
            'password': password,
            'created_at': datetime.utcnow()
        }
        result = db.users.insert_one(user_data)  # Insert new user
        user_data['_id'] = result.inserted_id  # Assign the generated ID
        return User(user_data)

# Prediction model to store and manage prediction records
class Prediction:
    @staticmethod
    def create(user_id, input_data, result):
        # Store a new prediction in the database
        prediction_data = {
            'user_id': user_id,
            'input_data': input_data,
            'result': result,
            'created_at': datetime.utcnow()
        }
        return db.predictions.insert_one(prediction_data)

    @staticmethod
    def get_user_predictions(user_id):
        # Retrieve all predictions made by the user, sorted by time (latest first)
        return list(db.predictions.find({'user_id': user_id}).sort('created_at', -1))

    @staticmethod
    def delete_prediction(prediction_id, user_id):
        # Delete a specific prediction belonging to a user
        return db.predictions.delete_one({'_id': ObjectId(prediction_id), 'user_id': user_id})
