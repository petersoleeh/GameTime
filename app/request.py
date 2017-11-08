import urllib.request,json
from .models import Match,League


base_url = None
fixture_url=None
league_url=None

def configure_request(app):
    global base_url,fixture_url,league_url
    base_url = app.config['GAME_WEEK_API']
    fixture_url = app.config['TEAM_URL']
    league_url=app.config['LEAGUE_URL']

def get_league():
    '''
    function to get the league in api
    '''

    print(league_url)
    with urllib.request.urlopen(league_url) as url:
        # print('<><><><>>NM<><><><><><>')
        get_league_data=url.read()
        get_league_response=json.loads(get_league_data)

        league_results=None

        league_results_list=get_league_response
        league_results=process_league(league_results_list)
        return league_results


def get_fixtures(name):
    '''
    function to get fixtures for a particular team
    '''
    get_fixtures_url=fixture_url.format(name)
    with urllib.request.urlopen(get_fixtures_url) as url:
        get_fixtures_data=url.read()
        get_fixtures_response=json.loads(get_fixtures_data)

        fixture_results=None

        fixture_results_list=get_fixtures_response
        fixture_results=process_results(fixture_results_list)
        print(len(fixture_results))
        return fixture_results


def get_week():
    '''
    function that gets the json response from the api
    '''
    with urllib.request.urlopen(base_url) as url:
        get_fixtures_data=url.read()
        get_fixtures_response=json.loads(get_fixtures_data)

        fixture_results=None

        if get_fixtures_response['week']:
            fixture_results_list=get_fixtures_response['week']
            fixture_results=process_results(fixture_results_list)

        return fixture_results

def process_league(league_list):
    '''
    function that process the league results and returns list of objects
    '''
    league_results=[]
    for match in league_list:
        pos=match.get('pos')
        team=match.get('team')
        team_id=match.get('team_id')
        points=match.get('points')
        played=match.get('played')
        gd=match.get('gd')


        if team:
            # print('<><><><><><>FGHJ<><><><><>')
            standing_object=League(pos,team,team_id,points,played,gd)
            league_results.append(standing_object)
    return league_results


def process_results(fixture_list):
    '''
    function that process the fixture results and returns list of objects
    '''
    fixture_results=[]
    for match in fixture_list:
        home_id=match.get('home_id')
        home=match.get('home')
        away_id=match.get('away_id')
        away=match.get('away')
        date=match.get('date')

        if home:
            # print('<><><><><><>FGHJ<><><><><>')
            match_object=Match(home,home_id,away,away_id,date)
            fixture_results.append(match_object)
    return fixture_results
