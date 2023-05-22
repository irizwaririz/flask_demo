from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('blog', __name__)

posts = [
    {'title': 'test', 'created': datetime.now(), 'body': 'test body'}
]

@bp.route('/')
def index():
    return render_template("blog/index.html", posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        created = datetime.now()

        posts.append({
            'title': title,
            'created': created,
            'body': body
        })
        
        return redirect(url_for("blog.index"))
    return render_template("blog/create.html")
