from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_week,get_fixtures,get_league








@main.route('/')
def index():
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


@main.route('/league')
def league():
    '''
    view function for league
    '''
    league=get_league()
    print(len(league))
    return render_template('league.html',league=league)
