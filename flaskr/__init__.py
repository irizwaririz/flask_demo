import os

from flask import Flask
from markupsafe import escape

from flaskr import db, blog

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    
    app.config.from_pyfile('config.py', silent=True)

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    @app.route('/hello')
    def hello_world():
        return "<h1>Hello, World!</h1>"

    # <script>alert("bad")</script>

    @app.route("/<path:name>")
    def hello_unsafe(name):
        return f"<h1>Hello, {name}!</h1>"

    # @app.route("/<path:name>")
    # def hello_safe(name):
    #     return f"<h1>Hello, {escape(name)}!</h1>"


    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
