from flask import Blueprint, render_template

admin = Blueprint('admin', __name__,
    template_folder='templates'
)

@admin.route('/')
def index():
    return "This is the admin"