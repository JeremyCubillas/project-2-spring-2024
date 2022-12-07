from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user

from application.database import User, db
from application.bp.authentication.forms import RegisterForm, LoginForm

authentication = Blueprint('authentication', __name__, template_folder='templates')


@authentication.route('/users')
def users():
    user_records = User.all()
    return render_template('users.html', users=user_records)


@authentication.route('/dashboard')
@login_required
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
        user = User.find_user_by_email(form.email.data)
        if user is None:
            user = User.create(form.email.data, form.password.data)
            user.save()
            return redirect(url_for('authentication.login'))
        else:
            flash('Already Registered')
    return render_template('registration.html', form=form)


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_user_by_email(form.email.data)
        if user is None:
            flash('User Not Found')
        elif user.check_password(form.password.data):
            flash('Welcome')
            user.authenticated = True
            user.save()
            login_user(user)

            return redirect(url_for('authentication.dashboard'))
        else:
            flash('Password Incorrect')
    return render_template('login.html', form=form)


@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage.homepage'))