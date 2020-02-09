from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from utils import mongo_utils
import os, json

app = Flask(__name__)
DIR = os.path.dirname(__file__) or '.'
app.secret_key = json.loads(open(DIR + "/secrets.JSON").read())['pythonsecretkey']

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/login")
def login():
    if 'user' in session:
        return redirect(url_for('root'))
    return render_template("login.html")

def require_login(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if 'user' not in session:
            flash('Please log in')
            return redirect(url_for('login'))
        else:
            return f(*args, **kwargs)
    return inner

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/auth_login", methods = ['POST'])
def auth_login():
    username = request.form["username"]
    password = request.form["password"]
    if mongo_utils.authenticate(username, password):
        session["user"] = username
        return redirect(url_for("root"))
    flash("invalid user or password")
    return redirect(url_for("login"))

@app.route("/signup")
def signup():
    if 'user' in session:
        return redirect(url_for('root'))
    return render_template("signup.html")

@app.route("/auth_signup", methods = ['POST'])
def auth_signup():
    username = request.form["username"]
    password = request.form["password"]
    if mongo_utils.register(username, password):
        session["user"] = username
        return redirect(url_for("root"))
    flash("user name already taken")
    return redirect(url_for("signup"))

@app.route('/logout')
@require_login
def logout():
    session.pop('user')
    return redirect(url_for('root'))

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
