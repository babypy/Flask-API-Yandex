import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "."))

import sqlite3

def get_db():
    conn = sqlite3.connect('db/API_requests.db')
    print('Успешное подключение к базе данных!')
    return conn