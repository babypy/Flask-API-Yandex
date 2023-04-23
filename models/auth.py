import os
import sys
import random
import json

sys.path.insert(1, os.path.join(sys.path[0], "."))

from db import get_db

import sqlite3


class AuthModel:
    def __init__(self):
        self.conn = get_db()
        self.cursor = self.conn.cursor()
        self.uid = None

    def authorization(self, user_data):
        try:
            login = user_data['login']
            password = user_data['password']
            self.cursor.execute(f'SELECT uid FROM Users WHERE login = {login} and password = {password}')
            result = self.cursor.fetchone()
            if result is not None and len(result) > 0:
                self.uid = result[0]
                return {"status": "success", "uid": self.uid}
            else:
                return {"status": "error", "message": "User not found"}
        except sqlite3.Error as error:
            return {"status": "error", "message": str(error)}

    def register_user(self, data):
        try:
            fields = ', '.join(data.keys())
            values = ', '.join(value for key, value in data.items())
            random_uid = random.randint(1, 10000)
            query = f"INSERT INTO Users ({fields}, uid) VALUES ({values}, {random_uid})"
            self.cursor.execute(query)
            self.conn.commit()
            return {"status": "success", "message": f"personal number: {random_uid}"}
        except sqlite3.Error as error:
            return {"status": "error", "message": str(error)}

    def authenticate_user(self, data):
        # пользователь вводит json в виде: login
        try:
            value = data.get('login')
            self.cursor.execute(f'SELECT * FROM Users WHERE login = {value}')
            user = self.cursor.fetchone()
            self.conn.commit()
            if user:
                return {"status": "success", "message": "The user is logged in to this page"}
            else:
                return {"status": "error", "message": "Invalid login"}
        except sqlite3.Error as e:
            return {"status": "error", "message": str(e)}

    def get_user_info(self, data):
        try:
            value = data.get('uid')
            self.cursor.execute(f'SELECT * FROM Users WHERE uid = ({value})')
            user = self.cursor.fetchone()
            if user:
                user_dict = {'id': user[0], 'name': user[1], 'email': user[2], 'username': user[3],
                             'city': user[4], 'password': user[5], 'login': user[6],
                             'phone': user[7], 'avatar': user[8], 'description': user[9], 'uid': user[10]}
                return {"status": "success", "user": user_dict}
            else:
                return {"status": "error", "message": "User not found"}
        except sqlite3.Error as e:
            return {"status": "error", "message": str(e)}

    def delete_user(self, data):
        try:
            value = data.get('uid')
            res = self.get_user_info(data)
            if res['status'] == 'error':
                return {"status": "error", "message": "User not found"}
            else:
                self.cursor.execute(f"DELETE FROM Users WHERE uid = ({value})")
                self.conn.commit()
                return {"status": "success", "message": "deleted successfully"}
        except sqlite3.Error as e:
            return {"status": "error", "message": str(e)}

    def __del__(self):
        self.conn.close()
