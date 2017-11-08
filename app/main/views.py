from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_week,get_fixtures
from ..models import Favourite,User
from flask_login import login_required,login_user, current_user








@main.route('/', methods = ["GET", "POST"])
def index():
    if request.method == 'POST':
        team_id = request.form.get('add_f')
        print(team_id)
        favourite_team = Favourite(team_id = team_id, user = current_user)
        return redirect ('/')
    """
    view function for the landing page
    """
    week_fixture=get_week()
    # print(len(week_fixture))
    return render_template('index.html',week_fixture=week_fixture)


@main.route('/team/<name>')
def team(name):
    '''
    view function for the dynamic route for each team
    '''
    team_fixtures=get_fixtures(name)
    return render_template('team.html',team_fixtures=team_fixtures)
