import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "."))

from db import get_db
from models.auth import AuthModel

import sqlite3


class UserModel:
    def __init__(self):
        self.conn = get_db()
        self.cursor = self.conn.cursor()
        self.uid = None
        self.auth = AuthModel()

    def description(self, user_data, description_data):
        try:
            res = self.auth.authorization(user_data)
            if res['status'] == 'error':
                return {"status": "error", "message": "Incorrect login or password"}
            else:
                self.uid = res['uid']
                self.cursor.execute(f"UPDATE Users SET description = {description_data['description']} "
                                    f"WHERE uid = {self.uid}")
                self.conn.commit()
                return {"status": "success", "message": "Description updated successfully"}
        except sqlite3.Error as error:
            return {"status": "error", "message": str(error)}

    def info_user(self, user_data, info_data):
        try:
            res = self.auth.authorization(user_data)
            if res['status'] == 'error':
                return {"status": "error", "message": "Incorrect login or password"}
            else:
                self.uid = res['uid']
                self.cursor.execute(f"UPDATE Users SET name = '{info_data['name']}', email = '{info_data['email']}',"
                                    f"username = '{info_data['username']}', city = '{info_data['city']}',"
                                    f"login = '{info_data['login']}', phone = '{info_data['phone']}'"
                                    f"WHERE uid = {self.uid}")
                self.conn.commit()
                return {"status": "success", "message": "Information updated successfully"}
        except sqlite3.Error as error:
            return {"status": "error", "message": str(error)}

    def password_user(self, user_data, password_data):
        try:
            res = self.auth.authorization(user_data)
            if res['status'] == 'error':
                return {"status": "error", "message": "Incorrect login or password"}
            else:
                self.uid = res['uid']
                self.cursor.execute(f"UPDATE Users SET password = '{password_data['password']}'"
                                    f"WHERE uid = {self.uid}")
                self.conn.commit()
                return {"status": "success", "message": "Password updated successfully"}
        except sqlite3.Error as error:
            return {"status": "error", "message": str(error)}

    def avatar_user(self, user_data, avatar_data):
        try:
            res = self.auth.authorization(user_data)
            if res['status'] == 'error':
                return {"status": "error", "message": "Incorrect login or password"}
            else:
                self.uid = res['uid']
                self.cursor.execute(f"UPDATE Users SET avatar = '{avatar_data['avatar']}' "
                                    f"WHERE uid = {self.uid}")
                self.conn.commit()
                return {"status": "success", "message": "Avatar updated successfully"}
        except sqlite3.Error as error:
            return {"status": "error", "message": str(error)}
