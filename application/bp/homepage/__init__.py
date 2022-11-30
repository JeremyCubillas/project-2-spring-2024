from flask import Blueprint, render_template

from application.database import User

bp_homepage = Blueprint('homepage', __name__, template_folder='templates')


@bp_homepage.route('/')
def homepage():
    return render_template('homepage.html')


@bp_homepage.route('/about')
def about():
    return render_template('about.html')


@bp_homepage.route('/users')
def users():
    user_records = User.all()
    return render_template('users.html', users=user_records)


@bp_homepage.route('/users/email/<email>')
def user_by_email(email):
    user = User.find_user_by_email(email)
    return render_template('user.html', user=user)


@bp_homepage.route('/users/<user_id>')
def user_by_id(user_id):
    user = User.find_user_by_id(user_id)
    return render_template('user.html', user=user)
