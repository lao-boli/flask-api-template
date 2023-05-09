from flask import (
    Blueprint, request, jsonify
)

from flaskr.models import User, base, Result, PageInfo
from flaskr.utils import get_page_info
from flaskr.exception import ResultError
from flaskr.api.auth import login_required

api = Blueprint('user', __name__, url_prefix='/user')
db = base.db


@api.route('/list', methods=['GET'])
@login_required
def get_users():
    users = User.list_users(request.args)
    return jsonify(Result.success(data=[user.to_dict() for user in users]))


@api.route('/page', methods=['GET'])
@login_required
def page_users():
    pagination = User.page(request.args)
    return jsonify(Result.success(get_page_info(pagination)))


@api.route('/get/<int:user_id>', methods=['GET'])
@login_required
def get_user(user_id):
    user = User.get_by_id(user_id)
    if user is None:
        return jsonify(Result.fail(msg='user not found'))
    return jsonify(user.to_dict())


@api.route('/add', methods=['POST'])
@login_required
def create_user():
    user = User.add(request.json)
    return jsonify(Result.success(msg='添加用户成功'))


@login_required
@api.route('/update', methods=['POST'])
def update_user():
    user = User.update(request.json)
    return jsonify(Result.success(msg='更新用户成功'))


@api.route('/delete/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    user = User.delete(user_id)
    return jsonify(Result.success(msg='删除用户成功'))


# not id

@api.route('/get', methods=['GET'])
@login_required
def get_user_no_id():
    return jsonify(Result.fail(msg='必须携带id'))


@api.route('/delete', methods=['GET'])
@login_required
def delete_user_no_id():
    return jsonify(Result.fail(msg='必须携带id'))
