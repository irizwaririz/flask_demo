from flask import Flask

from flaskr import blog


def create_app():
    app = Flask(__name__)
    
    @app.route('/hello')
    def hello_world():
        return "Hello world!"

    app.register_blueprint(blog.bp)

    return app
