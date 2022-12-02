from flask import Blueprint, render_template, redirect, url_for

from application.database import User
from application.bp.authentication.forms import RegisterForm

authentication = Blueprint('authentication', __name__, template_folder='templates')


@authentication.route('/users')
def users():
    user_records = User.all()
    return render_template('users.html', users=user_records)


@authentication.route('/dashboard')
def dashboard():
    user_records = User.all()
    return render_template('dashboard.html')


@authentication.route('/users/<user_id>')
def user_by_id(user_id):
    user = User.find_user_by_id(user_id)
    return render_template('user.html', user=user)


@authentication.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('dashboard', name='John'))
    return render_template('registration.html', form=form)
