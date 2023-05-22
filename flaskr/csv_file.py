import os

from flask import current_app, g


def get_csv_file():
    if not os.path.exists(current_app.config['CSV']):
        open(current_app.config['CSV'], 'x').close()

    if 'csv_file' not in g:
        g.csv_file = open(current_app.config['CSV'], 'a+')

    return g.csv_file

def close_csv(e=None):
    csv_file = g.pop('csv_file', None)

    if csv_file is not None:
        csv_file.close()

def init_app(app):
    app.teardown_appcontext(close_csv)
