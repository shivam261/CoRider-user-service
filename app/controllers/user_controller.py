from flask import request, jsonify
from app.models.users import User
from app import mongo, cache
import bcrypt
def get_user_by_id(id):
    user = mongo.db.users.find_one({'uid': id}, {'_id': 0, 'password': 0})
    if user:
        return jsonify(User(**user).to_dict()), 200
    else:
        return jsonify({"error": "User not found"}), 404

def update_user_by_id(id):
    data = request.json
    # dont allow updating uid
    if data['uid'] != id:
        return jsonify({"error": "Cannot update UID"}), 400
    if not data or 'email' not in data or 'name' not in data or 'password' not in data or 'uid' not in data:
        return jsonify({"error": "missing fields"}), 400
    
    data["password"] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    mongo.db.users.update_one({'uid': id}, {'$set': data})
    
    return jsonify({"message": "User updated successfully"}), 200

def delete_user_by_id(id):
    result = mongo.db.users.delete_one({'uid': id})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

def create_user():
    data = request.json
    if mongo.db.users.find_one({'uid': data['uid']}):
        return jsonify({"error": "UID already exists"}), 400
    new_user = User(**data)
    mongo.db.users.insert_one(new_user.to_dict())
    return jsonify({"message": "User created successfully"}), 201

@cache.cached(timeout=5, key_prefix="all_users")
def get_all_users():
    users = mongo.db.users.find({}, {'_id': 0, 'password': 0})
    user_list = [User(**user).to_dict() for user in users]
    return jsonify(user_list), 200
