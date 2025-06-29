from flask_login import UserMixin
from bson.objectid import ObjectId
from flask import current_app


class Note:
    @staticmethod
    def create(data, user_id):
        note = {
            "data": data,
            "user_id": ObjectId(user_id)
        }
        return current_app.mongo.notes.insert_one(note)

    @staticmethod
    def find_by_user(user_id):
        return list(current_app.mongo.notes.find({"user_id": ObjectId(user_id)}))


class User(UserMixin):
    def __init__(self, user_doc):
        self.id = str(user_doc['_id'])
        self.email = user_doc['email']
        self.password = user_doc['password']
        self.first_name = user_doc['first_name']

    @staticmethod
    def get_by_email(email):
        user_doc = current_app.mongo.users.find_one({"email": email})
        return User(user_doc) if user_doc else None

    @staticmethod
    def get_by_id(user_id):
        try:
            user_doc = current_app.mongo.users.find_one({"_id": ObjectId(user_id)})
            return User(user_doc) if user_doc else None
        except Exception:
            return None

    @staticmethod
    def create(email, first_name, password):
        user = {
            "email": email,
            "first_name": first_name,
            "password": password
        }
        result = current_app.mongo.users.insert_one(user)
        user['_id'] = result.inserted_id
        return User(user)