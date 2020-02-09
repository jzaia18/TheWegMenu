from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from utils import mongo_utils, wegmans_utils
from utils import recipe_maker
from utils import Alternatives
import os, json

app = Flask(__name__)
DIR = os.path.dirname(__file__) or '.'
app.secret_key = json.loads(open(DIR + "/secrets.JSON").read())['pythonsecretkey']

DAYS = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']

def require_login(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if 'user' not in session:
            flash('Please log in')
            return redirect(url_for('login'))
        else:
            return f(*args, **kwargs)
    return inner

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/login")
def login():
    if 'user' in session:
        return redirect(url_for('root'))
    return render_template("login.html")

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
    flash("Invalid user or password. Please try again.")
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

@app.route('/planner')
@require_login
def calendar():
    cal = mongo_utils.get_calendar(session['user'])

    for day in DAYS:
        if day in cal:
            cal[day] = [mongo_utils.get_recipe_by_id(rid) for rid in cal[day]]
        else:
            cal[day] = []

    return render_template('calendar.html', calendar = cal)

@app.route('/search', methods = ['POST'])
@require_login
def search():
    if 'query' not in request.form:
        flash("Please include a query")
        redirect(url_for("root"))

    query = request.form['query']
    results = mongo_utils.get_recipes_by_food(query, results=5)

    for hit in results:
        hit['ingredientLines'] = recipe_maker.translate(hit['ingredientLines'])
        #hit['alternative_caution'] = Alternatives.filter_recipe([x[1] for x in hit['ingredientLines']], [])

    return render_template('search.html', results=results, query=query)

@app.route('/add_recipe', methods = ["POST"])
def add_recipe():
    mongo_utils.add_recipe_to_calendar(request.form["recipeid"], request.form["day"], session['user'])
    return ''

@app.route('/remove_recipe', methods = ['POST'])
@require_login
def remove_recipe():
    mongo_utils.remove_recipe_from_calendar(request.form['recipe_id'], request.form['day'], session['user'])
    return redirect(url_for("calendar"))

@app.route('/prefs')
@require_login
def prefs():
    return render_template('preferences.html')

@app.route('/update_prefs', methods=['POST'])
@require_login
def update_prefs():
    #return redirect(url_for("root"))
    return str(request.form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
