from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_week








@main.route('/')
def index():
    """
    view function for the landing page
    """
    week_fixture=get_week()
    print(len(week_fixture))
    return render_template('index.html',week_fixture=week_fixture)
