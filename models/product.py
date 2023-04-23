import os
import sys
import json

sys.path.insert(1, os.path.join(sys.path[0], "."))

from db import get_db
from models.auth import AuthModel

import sqlite3


class ProductModel:
    def __init__(self):
        self.conn = get_db()
        self.cursor = self.conn.cursor()
        self.uid = None
        self.id = None
        self.auth = AuthModel()

    def new_category(self, user_data, product_data):
        try:
            res = self.auth.authorization(user_data)
            if res['status'] == 'error':
                return {"status": "error", "message": "Incorrect login or password"}
            else:
                self.uid = res['uid']
                self.cursor.execute(f"INSERT INTO Category_products (category, "
                                    f"uid_creator) VALUES ({product_data['category']}, {self.uid})")
                self.conn.commit()
                return {"status": "success", "message": "Category added successfully"}
        except sqlite3.Error as error:
            return {"status": "error", "message": str(error)}

    def del_category(self, user_data, product_data):
        try:
            res = self.auth.authorization(user_data)
            if res['status'] == 'error':
                return {"status": "error", "message": "Incorrect login or password"}
            else:
                self.uid = res['uid']
                self.cursor.execute(f"SELECT * FROM Category_products WHERE "
                                    f"category = {product_data['category']} AND uid_creator = {self.uid}")
                result = self.cursor.fetchone()
                if result:
                    self.cursor.execute(f"DELETE FROM Category_products WHERE id = {result[0]}")
                    self.conn.commit()
                return {"status": "success", "message": "Category removed"}
        except sqlite3.Error as error:
            return {"status": "error", "message": str(error)}

    def new_product(self, user_data, product_data):
        try:
            sp = []
            for key, value in product_data.items():
                sp.append(value)
            res = self.auth.authorization(user_data)
            if res['status'] == 'error':
                return {"status": "error", "message": "Incorrect login or password"}
            else:
                self.uid = res['uid']
                self.cursor.execute("INSERT INTO Products (uid_user, title, id_category, information, price) "
                                    "VALUES (?, ?, (SELECT id FROM Category_products), ?, ?)",
                                    (self.uid, sp[0], sp[2], sp[3]))
                self.conn.commit()
                return {"status": "success", "message": "Product added successfully"}
        except sqlite3.Error as error:
            return {"status": "error", "message": str(error)}

    def del_product(self, user_data, product_data):
        try:
            res = self.auth.authorization(user_data)
            if res['status'] == 'error':
                return {"status": "error", "message": "Incorrect login or password"}
            else:
                self.uid = res['uid']
                self.cursor.execute(f"SELECT * FROM Products WHERE "
                                    f"id = {product_data['id']} AND uid_user = {self.uid}")
                result = self.cursor.fetchone()
                if result:
                    self.cursor.execute(f"DELETE FROM Products WHERE id = {result[0]}")
                    self.conn.commit()
                return {"status": "success", "message": "The product has been removed"}
        except sqlite3.Error as error:
            return {"status": "error", "message": str(error)}

    def find_product(self, product_data):
        try:
            value = product_data.get('id')
            self.cursor.execute(f'SELECT * FROM Products WHERE id = ({value})')
            result = self.cursor.fetchone()
            if result:
                result_dict = {'id': result[0], 'uid_user': result[1], 'title': result[2], 'id_category': result[3],
                               'information': result[4], 'price': result[5]}
                return {"status": "success", "product": result_dict}
            else:
                return {"status": "error", "message": "Product not found"}
        except sqlite3.Error as e:
            return {"status": "error", "message": str(e)}
