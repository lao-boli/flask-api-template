from flask import (
    Blueprint, request, jsonify
)

from flaskr.models import User, base,Result,PageInfo
from flaskr.utils  import get_page_info

api = Blueprint('user', __name__,url_prefix='/user')
db = base.db


@api.route('/list', methods=['GET'])
def get_users():
    users = User.list_users(request.args)
    return jsonify(Result.success([user.to_dict() for user in users]))


@api.route('/page', methods=['GET'])
def page_users():
    pagination = User.page(request.args)
    return jsonify(Result.success(get_page_info(pagination)).to_dict())


@api.route('/get/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict())


@api.route('/add', methods=['POST'])
def create_user():
    user = User.add(request.json)
    return jsonify(Result.success('添加用户成功'))


@api.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    user = User.update(request.json, user_id)
    return jsonify(Result.success('更新用户成功'))


@api.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    User.delete(user_id)
    return jsonify(Result.success('删除用户成功'))
