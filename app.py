from flask import Flask
from flask import request
from flask import send_from_directory
from flask import redirect, render_template, abort
import io
import os
import sys

app = Flask(__name__)

@app.route("/")
def index_page():
    return "Hi from Azure"

@app.route('/map')
def tube_map():
    return render_template('tubemap.html')