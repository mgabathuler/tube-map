import os

from flask import Flask
from flask import (
    Blueprint, flash, g,
    redirect, render_template,
    request, session, url_for
)

import basehtml

app = Flask(__name__)
app.register_blueprint(basehtml.bp)

@app.route("/")
def index_page():
    return render_template('basehtml/main.html')

@app.route('/map')
def tube_map():
    return render_template('basehtml/tubemap.html')