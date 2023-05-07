from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import os
from jinja2 import Environment

from token_manager import generate_token, get_username_from_token, check_token
from db_handler import database_handler as dbh
from password_handler import *
from validations import validate_email, validate_password

app = Flask(__name__)
db = dbh("networking.db")

app.jinja_env.filters['strfttime'] = datetime.strftime
env = Environment()
env.filters['strftime'] = datetime.strftime
secret_key = os.urandom(32)
app.secret_key = secret_key


def error_handler():
    flash(("User timed out. Please try again", "danger"))
    return redirect(url_for("login"))


@app.route('/')
def landing_check():  # Redirection to the login page
    try:
        # To make sure that there's no token created
        token = session['token']
        username = get_username_from_token(token)
        return redirect(url_for('dashboard'))
    except KeyError:
        return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    print(request.method)
    result = ""
    if request.method == 'POST':
        uname = request.form["username"]
        password = request.form["password"]
        uname_check = db.username_exists(uname)
        if uname_check:
            db_object = db.get_user(uname)
            db_password = db_object.password
            pass_state = check_password(password, db_password)
            if pass_state:  # If the password is correct
                uname = db_object.username
                flash("Logged in successfully", "success")
                user = db.get_user(uname)
                session["token"] = generate_token(user.username, 120)
                return redirect(url_for('dashboard', username=user.username))

            else:
                flash(("Wrong password", "danger"))
                return redirect(url_for('login'))

        else:
            flash(("User does not exist", "danger"))
            return redirect(url_for('login'))

    else:
        return render_template("login.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    message = ""
    print(request.method)
    if request.method == "POST":  # Register button pressed
        email = request.form["email"]
        password = request.form["psw"]
        password2 = request.form["psw-repeat"]
        username = request.form["username"]
        print(email, 121)
        if validate_email(email):
            if not db.username_exists(username):
                print("Username is there")
                print(db.email_exists(email))
                if not db.email_exists(email):
                    if validate_password(password):
                        if password == password2:
                            hashed_pwd = hash_password(password)
                            db.insert_user(email, username, hashed_pwd)
                            flash(("User created successfully", "success"))
                            return redirect(url_for("login"))

                        else:
                            flash(("Passwords do not match", "danger"))
                            return redirect(url_for("registration"))
                    else:
                        flash(("The password has to be between 8 and 32 characters", "danger"))
                        return redirect(url_for("registration"))
                else:
                    flash(("Email already exists", "danger"))
                    return redirect(url_for("registration"))
            else:
                flash(("The username already exists", "danger"))
                return redirect(url_for("registration"))
        else:
            print("why?")
            flash(("Please enter a valid email address", "danger"))
            return redirect(url_for("registration"))
    else:
        return render_template("registration.html")


@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    try:
        token = session["token"]
        username = get_username_from_token(token)
        print(username)
        print(request.method)
        if request.method == "POST":
            title = request.form["title"]
            content = request.form["content"]
            print(title)
            print(content)
            if title.strip() != "":
                if content.strip() != "":
                    temp_result = db.insert_post(username, title, content)
                    if not temp_result:
                        flash(("The title already exists", "danger"))
                        return redirect(url_for("new_post"))
                    else:
                        flash(("Post added successfully", "success"))
                        return redirect(url_for("my_profile", username=username))
                else:
                    flash(("The content cannot be empty", "danger"))
            else:
                flash(("The title cannot be empty", "danger"))

        elif request.method == "GET":
            return render_template("new_post.html", username=username)

    except KeyError:
        return error_handler()


@app.route("/dashboard", methods=["GET"])
def dashboard():
    try:
        token = session["token"]
        username = get_username_from_token(token)
        # Defining the variable 'sort_by'
        sort_by = request.args.get('sort_by', default="", type=str)
        # Run only when the user is given an input
        if request.method == "GET":
            search_in = request.args.get("search")
            # To avoid running into an error when querying
            if search_in is None:
                # To avoid running into an error when querying
                search_in = ""
            posts = db.search_posts_by_x(sort_by, search_in)
            return render_template("post_template.html",username = username, posts = posts)

    except KeyError:
        flash(("User timed out. Please try again", "danger"))
        return redirect(url_for("login"))


@app.route("/my_profile")
def my_profile():
    try:
        token = session["token"]
        username = get_username_from_token(token)
        user = db.get_user(username)
        posts = db.get_own_posts(username)
        return render_template("profile.html", posts=posts, username=username, user=user)

    except KeyError:
        return error_handler()


@app.route("/change_password", methods=["POST", "GET"])
def change_password():
    try:
        token = session["token"]
        username = get_username_from_token(token)
        if check_token(token):
            if request.method == "POST":
                user = db.get_user(username)
                old_pw = request.form["old_pw"]
                new_pw_1 = request.form["new_pw_1"]
                new_pw_2 = request.form["new_pw_2"]
                if check_password(old_pw, user.password):
                    if validate_password(new_pw_1):
                        if new_pw_1 == new_pw_2:
                            temp_pass = hash_password(new_pw_1)
                            db.change_pswd(username, temp_pass)
                            flash(("Password changed successfully", "success"))
                            return redirect(url_for("dashboard"))

                        else:
                            flash(("New passwords do not match", "danger"))
                            return redirect(url_for("change_password"))
                    else:
                        flash(("The new password must be between 8-32 characters", "danger"))
                        return redirect(url_for("change_password"))
                else:
                    print("stuck at here")
                    flash(("Wrong password", "danger"))
                    return redirect(url_for("change_password"))

            elif request.method == "GET":
                return render_template("change_password.html", username = username)



    except KeyError:
        return error_handler()


@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))


@app.route("/add_accl/<int:post_id>")
def add_like(post_id):
    try:
        token = session['token']
        if check_token(token):
            db.add_like_or_dislike(post_id, "like")
            return redirect(request.referrer)
        else:
            return error_handler()
    except KeyError:
        return error_handler()


@app.route("/add_dece/<int:post_id>")
def add_dislike(post_id):
    try:
        token = session['token']
        if check_token(token):
            db.add_like_or_dislike(post_id, "dislike")
            return redirect(request.referrer)
        else:
            return error_handler()
    except KeyError:
        return error_handler()


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    try:
        token = session["token"]
        if check_token(token):
            db.delete_post(post_id)
            return redirect(request.referrer)
            flash(("Post was deleted successfully", "success"))
        else:
            return error_handler()
    except KeyError:
        return error_handler()



if __name__ == "__main__":
    app.debug = True  # setting the debugging option for the application instance
    app.run()
