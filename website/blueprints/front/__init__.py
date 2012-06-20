from flask import Blueprint, render_template

site = Blueprint('site', __name__,
    template_folder = 'templates',
    #static_folder = 'static',
)

@site.route("/")
def hello():
    return render_template('front/index.html')