import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "."))

from models.auth import AuthModel
from utils import parse_form_data, parse_form_elem


class AuthApi():
    def __init__(self):
        super().__init__()
        self.auth = AuthModel()

    def get_users(self, req):
        method = req.method
        if method == 'POST':
            data = parse_form_data(req, 'register_user')
            res = self.auth.register_user(data)
            if res['status'] == 'success':
                return f"User registered successfully, {res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def authenticate(self, req):
        method = req.method
        if method == 'GET':
            data = parse_form_elem(req, 'authenticate_user')
            res = self.auth.authenticate_user(data)
            # Проверяем данные и возвращаем ответ
            if res['status'] == 'success':
                return f"Запрос выполнен: {res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def info_user(self, req):
        method = req.method
        if method == 'GET':
            data = parse_form_elem(req, 'get_user_info')
            res = self.auth.get_user_info(data)
            if res['status'] == 'success':
                return f"{res['user']}"
            else:
                return f"Error: {res['message']}"
            # Проверяем данные и возвращаем ответ
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def del_user(self, req):
        method = req.method
        if method == 'POST':
            data = parse_form_data(req, 'delete_user')
            res = self.auth.delete_user(data)
            if res['status'] == 'success':
                return f"User {res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def authorization(self, req):
        method = req.method
        if method == 'POST':
            user_data = req.json
            res = self.auth.authorization(user_data)
            if res['status'] == 'success':
                return f"Uid: {res['uid']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'
