from flask import Blueprint, render_template
from flask import render_template, request, url_for, redirect, flash, session, Flask
from flask_login import LoginManager,  login_user, current_user, logout_user
from models.user import User, Images, Follows
from werkzeug.security import generate_password_hash, check_password_hash
from app import app

login_blueprint = Blueprint('login',
                            __name__,
                            template_folder='templates/login')

@login_blueprint.route('/', methods=['GET'])
def index():
    return render_template('signin.html')

# Method to Login 2 :: Login Manager
# This callback is used to reload the user object from the user ID stored in the session
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get_or_none(User.id == user_id)

@login_blueprint.route("/signin", methods=['POST'])
def signin():
    # breakpoint()
        username = request.form.get('username')
        password_to_check = request.form.get('password')

        user = User.get_or_none(User.username == username)

        if not user:
            flash('There is no one with that Username. Please check')
            return redirect(url_for('login.index'))

        hashed_password = user.password

        if not check_password_hash(hashed_password, password_to_check):
            flash('Incorrect password. Please try again.')
            return redirect(url_for('login.index'))


# user profile page
@login_blueprint.route("/userpage", methods=["GET"])
def main_userpage():
    # user = User.get_by_id(user_id)
    return render_template("userpage.html")

