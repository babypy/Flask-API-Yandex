import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "."))

from flask import render_template


def routing(app):
    @app.route('/product', methods=("GET", "POST"))
    def product():
        return render_template("product/index.html")

    @app.route('/auth', methods=("GET", "POST"))
    def auth():
        return render_template("auth/index.html")

    @app.route('/user', methods=("GET", "POST"))
    def user():
        return render_template("user/index.html")
