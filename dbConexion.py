import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext

DATABASE = "Petropolis.db"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_connection(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def finish_app(app):
    app.teardown_appcontext(close_connection)

def init_app(app):
    with app.app_context():
        db = get_db()
        return db

