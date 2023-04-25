import os

from flask import Flask

from flaskr import csv_file, blog

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        CSV=os.path.join(app.instance_path, 'flaskr.csv')
    )
    
    app.config.from_pyfile('config.py', silent=True)

    os.makedirs(app.instance_path, exist_ok=True)

    csv_file.init_app(app)

    @app.route('/hello')
    def hello_world():
        return "<h1>Hello, World!</h1>"

    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
