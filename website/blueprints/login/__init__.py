from flask import Blueprint, session, redirect, request, url_for, render_template

bp = Blueprint('login', __name__)


@bp.route("/")
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))