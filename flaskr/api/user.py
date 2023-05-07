from flask import (
    Blueprint, request, jsonify
)

from flaskr.models import User, base, Result, PageInfo
from flaskr.utils import get_page_info

api = Blueprint('user', __name__, url_prefix='/user')
db = base.db


@api.route('/list', methods=['GET'])
def get_users():
    users = User.list_users(request.args)
    return jsonify(Result.success(data=[user.to_dict() for user in users]))


@api.route('/page', methods=['GET'])
def page_users():
    pagination = User.page(request.args)
    return jsonify(Result.success(get_page_info(pagination)))


@api.route('/get/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get(user_id)
    if user is None:
        return jsonify(Result.fail(msg='user not found'))
    return jsonify(user.to_dict())


@api.route('/add', methods=['POST'])
def create_user():
    user = User.add(request.json)
    return jsonify(Result.success(msg='添加用户成功'))


@api.route('/update', methods=['POST'])
def update_user():
    user = User.update(request.json)
    return jsonify(Result.success(msg='更新用户成功'))


@api.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    User.delete(user_id)
    return jsonify(Result.success(msg='删除用户成功'))
