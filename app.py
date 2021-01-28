import os

from flask import Flask
from flask import (
    Blueprint, flash, g,
    redirect, render_template,
    request, session, url_for,
    send_from_directory
)

import basehtml
import datafiles as df

app = Flask(__name__)
app.register_blueprint(basehtml.bp)

@app.route("/")
def index_page():
    return render_template('basehtml/main.html')

@app.route('/map')
def tube_map():
    g.datafiles = df.listDataFiles()
    g.loadfile = "demo"
    if request.args.get('file-selector'):
        g.loadfile = request.args.get('file-selector')

    return render_template('basehtml/tubemap.html')

@app.route('/data/<datafile>')
def tube_data(datafile):
    filename = ".".join((datafile, "json"))
    return send_from_directory(
        '/srv/data',
        filename=filename,
        mimetype="application/json")