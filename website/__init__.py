from flask import Flask, request, render_template, abort
from utility import timestamped
import re
import os

app = Flask(__name__)

env = os.getenv('mm_env', 'production')
if env == 'dev':
    app.debug = True

app.jinja_env.filters['timestamped'] = timestamped

app.jinja_env.globals.update({
    'env': env
})


@app.route("/")
def hello():
    return render_template('index.html')

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
