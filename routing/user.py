import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "."))

from flask import request, Blueprint
from api.user import UserApi


bp = Blueprint("user", __name__, url_prefix="/api/user")


@bp.route('/description', methods=("GET", "POST"))
def change():
    req = request
    api = UserApi()
    return api.description_user(req)


@bp.route('/info', methods=("GET", "POST"))
def change_info():
    req = request
    api = UserApi()
    return api.information_user(req)


@bp.route('/password', methods=("GET", "POST"))
def change_password():
    req = request
    api = UserApi()
    return api.new_password(req)


@bp.route('/avatar', methods=("GET", "POST"))
def change_avatar():
    req = request
    api = UserApi()
    return api.new_avatar(req)