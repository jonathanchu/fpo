from flask import Flask, request, render_template, abort
from utility import timestamped
import re
import os

from blueprints.admin import admin
from blueprints.front import site

app = Flask(__name__)

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(site)

env = 'dev'
if env == 'dev':
    app.debug = True

app.jinja_env.filters['timestamped'] = timestamped

app.jinja_env.globals.update({
    'env': env
})


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
