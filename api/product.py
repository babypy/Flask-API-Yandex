import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "."))

from models.product import ProductModel
from utils import parse_form_data, parse_form_elem


class ProductApi():
    def __init__(self):
        super().__init__()
        self.auth = ProductModel()

    def get_category(self, req):
        method = req.method
        if method == 'POST':
            user_data = parse_form_data(req, 'authorization')
            product_data = parse_form_data(req, 'new_category')
            res = self.auth.new_category(user_data, product_data)
            if res['status'] == 'success':
                return f"{res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def delete_category(self, req):
        method = req.method
        if method == 'POST':
            user_data = parse_form_data(req, 'authorization')
            product_data = parse_form_data(req, 'category')
            print(product_data)
            print(user_data)
            res = self.auth.del_category(user_data, product_data)
            if res['status'] == 'success':
                return f"{res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def new_product(self, req):
        method = req.method
        if method == 'POST':
            user_data = parse_form_data(req, 'authorization')
            product_data = parse_form_data(req, 'new_product')
            res = self.auth.new_product(user_data, product_data)
            if res['status'] == 'success':
                return f"{res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def delete_product(self, req):
        method = req.method
        if method == 'POST':
            user_data = parse_form_data(req, 'authorization')
            product_data = parse_form_data(req, 'id_product')
            res = self.auth.del_product(user_data, product_data)
            if res['status'] == 'success':
                return f"{res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def get_info_product(self, req):
        method = req.method
        if method == 'GET':
            product_data = parse_form_elem(req, 'id_product')
            res = self.auth.find_product(product_data)
            if res['status'] == 'success':
                return f"{res['product']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'
