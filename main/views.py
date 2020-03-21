from main import app
from flask import request, redirect, url_for, render_template, flash, session

@app.route("/")
def index():
    return render_template("index.html")

