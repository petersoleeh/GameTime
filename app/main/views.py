from flask import render_template, request, redirect, url_for, abort
from . import main


@main.route('/')
def index():
    """
    view function for the landing page
    """
    return render_template('index.html')
