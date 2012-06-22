from flask import Blueprint, render_template

bp = Blueprint('admin', __name__,
    template_folder='templates'
)

@bp.route('/')
def index():
    return "This is the admin"