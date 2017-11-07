import urllib.request,json
from .models import Match


base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['GAME_WEEK_API']


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
            print('<><><><><><>FGHJ<><><><><>')
            match_object=Match(home,home_id,away,away_id,date)
            fixture_results.append(match_object)
    return fixture_results
