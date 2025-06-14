from flask import Blueprint, request
from app.controllers import user_controller
from app import limiter

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/<id>', methods=['PUT', 'GET', 'DELETE'])
@limiter.limit("80 per minute")
def user_detail(id):
    if request.method == 'PUT':
        return user_controller.update_user_by_id(id)
    elif request.method == 'GET':
        return user_controller.get_user_by_id(id)
    elif request.method == 'DELETE':
        return user_controller.delete_user_by_id(id)

@user_bp.route('/', methods=['POST', 'GET'])
@limiter.limit("100 per minute")
def user_list():
    if request.method == 'POST':
        return user_controller.create_user()
    elif request.method == 'GET':
        return user_controller.get_all_users()
