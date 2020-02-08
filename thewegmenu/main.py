from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/")
def root():
    return render_template("base.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
