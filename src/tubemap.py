from flask import Flask
from flask import request
from flask import send_from_directory
from flask import redirect, render_template, abort
import io
import os
import sys

app = Flask(__name__)
root_path = None

@app.route('/')
def hello_world():
    return 'Hello, to the qrcode generator!'