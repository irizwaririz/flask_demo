from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template("base.html")
    
    @app.route('/hello')
    def hello_world():
        return "Hello world!"

    return app
