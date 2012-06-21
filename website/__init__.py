from flask import Flask, request, render_template, abort
from utility import timestamped
import re
import os

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

from blueprints.admin import admin
from blueprints.front import site

app = Flask(__name__)

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(site)

app.config.from_object('website.settings')
db = SQLAlchemy(app)

env = os.getenv('mm_env', 'production')
if env == 'dev':
    app.debug = True

app.jinja_env.filters['timestamped'] = timestamped

app.jinja_env.globals.update({
    'env': env
})

# should moves this to models.py when app gets fleshed out more
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    pw_hash = Column(String(128), unique=True)

    def __init__(self, username=None, email=None):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

class Group(db.Model):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String())

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Group %r>' % (self.name)

try:
    db.create_all()
except Exception:
    pass

@app.route("/i/<gid>/<path:path>")
def image(gid, path):
    app.logger.debug("Image request -  gid: %s, path: %s" % (gid, path))
    return ''

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

@app.route("/robots.txt")
def robots():
    return app.send_static_file("robots.txt")

@app.route("/static/<directory>/<path:filepath>")
def static_versioned(directory, filepath):
    if filepath.find('.v') != -1:
        filepath = re.sub('\.v\d+', '', filepath)

    return app.send_static_file(directory+'/'+filepath)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
