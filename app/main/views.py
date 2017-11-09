from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_week,get_fixtures,get_league
from ..models import Favourite,User
from flask_login import login_required,login_user, current_user


@main.route('/', methods = ["GET", "POST"])
def index():
    """
    view function for the landing page
    """
    favourites=[]
    week_fixture=get_week()
    if current_user.is_authenticated:
        if request.method == 'POST':
            team_id = request.form.get('add_f')
            # print(team_id)

            favourite_team = Favourite(team_id = team_id, user = current_user)
            favourite_team.add_favorites()
            return redirect ('/')

        favourites=Favourite.query.filter_by(user=current_user)
        # print(len(week_fixture))
        return render_template('index.html',week_fixture=week_fixture,favourites=favourites)
    return render_template('index.html',week_fixture=week_fixture,favourites=favourites)


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
