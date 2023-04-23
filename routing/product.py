import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "."))

from flask import request, Blueprint
from api.product import ProductApi


bp = Blueprint("product", __name__, url_prefix="/api/product")


@bp.route('/category', methods=("GET", "POST"))
def get_category():
    req = request
    api = ProductApi()
    return api.get_category(req)


@bp.route('/delete_category', methods=("GET", "POST"))
def delete_category():
    req = request
    api = ProductApi()
    return api.delete_category(req)


@bp.route('/product', methods=("GET", "POST"))
def new_product():
    req = request
    api = ProductApi()
    return api.new_product(req)


@bp.route('/delete_product', methods=("GET", "POST"))
def delete_product():
    req = request
    api = ProductApi()
    return api.delete_product(req)


@bp.route('/get_product', methods=("GET", "POST"))
def get_product():
    req = request
    api = ProductApi()
    return api.get_info_product(req)
