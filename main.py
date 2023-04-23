import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "."))

from flask import Flask
from routing import auth, product, user
from templates.route import routing

app = Flask(__name__)

app.register_blueprint(auth.bp)
app.register_blueprint(product.bp)
app.register_blueprint(user.bp)
routing(app)

if __name__ == '__main__':
    app.run()
