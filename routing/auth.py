import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "."))

from flask import request, Blueprint
from api.auth import AuthApi


bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@bp.route('/signup', methods=("GET", "POST"))
def get():
    req = request
    api = AuthApi()
    return api.get_users(req)


@bp.route('/authenticate', methods=("GET", "POST"))
def check():
    req = request
    api = AuthApi()
    return api.authenticate(req)


@bp.route('/information', methods=("GET", "POST"))
def info():
    req = request
    api = AuthApi()
    return api.info_user(req)


@bp.route('/delete', methods=("GET", "POST"))
def del_user():
    req = request
    api = AuthApi()
    return api.del_user(req)


@bp.route('/authorization', methods=("GET", "POST"))
def authorization():
    req = request
    api = AuthApi()
    return api.authorization(req)

