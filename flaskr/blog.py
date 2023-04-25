import csv
from datetime import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.csv_file import get_csv_file

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    csv_file = get_csv_file()
    csv_file.seek(0)
    reader = csv.reader(csv_file)

    posts = []
    for row in reader:
        posts.append({
            "created": row[0],
            "title": row[1],
            "body": row[2],
        })

    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            csv_file = get_csv_file()
            writer = csv.writer(csv_file)

            writer.writerow([datetime.now(), title, body])

            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
