from flask import render_template,session,redirect,url_for
from datetime import datetime

from . import main

@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')
