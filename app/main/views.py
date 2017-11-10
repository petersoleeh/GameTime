from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_week,get_fixtures,get_league,get_search
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
            favourites_obj=Favourite.query.filter_by(user=current_user).all()
            team_id = request.form.get('add_f')
            team_id2=request.form.get('del_f')
            if team_id2:
                favourite_del = Favourite.query.filter_by(team_id=team_id2).first()
                favourite_del.delete_favourite()
            fav_list=[]
            for fav in favourites_obj:
                asdf=fav.team_id
                fav_list.append(asdf)
            if team_id not in fav_list:
                favourite_team = Favourite(team_id = team_id, user = current_user)
                favourite_team.add_favorites()
            return redirect ('/')
        favourites=Favourite.query.filter_by(user=current_user)
        return render_template('index.html',week_fixture=week_fixture,favourites=favourites)
    return render_template('index.html',week_fixture=week_fixture,favourites=favourites)

@main.route('/team/<name>', methods = ["GET", "POST"])
def team(name):
    '''
    view function for the dynamic route for each team
    '''
    team_fixtures=get_fixtures(name)
    favourites=[]
    # week_fixture=get_week()
    if current_user.is_authenticated:
        if request.method == 'POST':
            favourites_obj=Favourite.query.filter_by(user=current_user).all()
            team_id = request.form.get('add_f')
            team_id2=request.form.get('del_f')
            if team_id2:
                favourite_del = Favourite.query.filter_by(team_id=team_id2).first()
                favourite_del.delete_favourite()
            fav_list=[]
            for fav in favourites_obj:
                asdf=fav.team_id
                fav_list.append(asdf)
            if team_id not in fav_list:
                favourite_team = Favourite(team_id = team_id, user = current_user)
                favourite_team.add_favorites()
        favourites=Favourite.query.filter_by(user=current_user).all()
        return render_template('team.html',team_fixtures=team_fixtures,favourites=favourites)
    return render_template('team.html',team_fixtures=team_fixtures,favourites=favourites)



@main.route('/league/<name>',methods=["GET","POST"])
def league(name):
    '''
    view function for league
    '''
    league=get_league(name)
    favourites=[]
    # week_fixture=get_week()
    if current_user.is_authenticated:
        if request.method == 'POST':
            favourites_obj=Favourite.query.filter_by(user=current_user).all()
            team_id = request.form.get('add_f')
            team_id2=request.form.get('del_f')
            if team_id2:
                favourite_del = Favourite.query.filter_by(team_id=team_id2).first()
                favourite_del.delete_favourite()
            fav_list=[]
            for fav in favourites_obj:
                asdf=fav.team_id
                fav_list.append(asdf)
            if team_id not in fav_list:
                favourite_team = Favourite(team_id = team_id, user = current_user)
                favourite_team.add_favorites()
                return render_template('league.html',league=league,favourites=favourites)
        favourites=Favourite.query.filter_by(user=current_user).all()
        return render_template('league.html',league=league,favourites=favourites)
    return render_template('league.html',league=league,favourites=favourites)


@main.route('/search',methods=['POST','GET'])
def search():
    '''
    view function for the search
    '''
    if request.method == 'POST':
        named = request.form.get('search')
        results=get_search(named)


    return render_template('search.html',name=results)
