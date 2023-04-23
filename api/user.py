import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "."))

from models.user import UserModel
from utils import parse_form_data, parse_form_elem


class UserApi():
    def __init__(self):
        super().__init__()
        self.user = UserModel()

    def description_user(self, req):
        method = req.method
        if method == 'POST':
            user_data = parse_form_data(req, 'authorization')
            description_data = parse_form_data(req, 'description')
            res = self.user.description(user_data, description_data)
            if res['status'] == 'success':
                return f"{res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def information_user(self, req):
        method = req.method
        if method == 'POST':
            user_data = parse_form_data(req, 'authorization')
            info_data = parse_form_data(req, 'info')
            res = self.user.password_user(user_data, info_data)
            if res['status'] == 'success':
                return f"{res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def new_password(self, req):
        method = req.method
        if method == 'POST':
            user_data = parse_form_data(req, 'authorization')
            password_data = parse_form_data(req, 'new_password')
            res = self.user.password_user(user_data, password_data)
            if res['status'] == 'success':
                return f"{res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'

    def new_avatar(self, req):
        method = req.method
        if method == 'POST':
            user_data = parse_form_data(req, 'authorization')
            avatar_data = parse_form_data(req, 'new_avatar')
            res = self.user.avatar_user(user_data, avatar_data)
            if res['status'] == 'success':
                return f"{res['message']}"
            else:
                return f"Error: {res['message']}"
        else:
            # Если метод запроса не совсем правильный, возвращаем ошибку
            return 'Invalid request method'
