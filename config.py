import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://soleeh:soleeh..@localhost/gametime'
    GAME_WEEK_API='https://gtime-api.herokuapp.com/teams/week/12'
    TEAM_URL='https://gtime-api.herokuapp.com/teams/{}'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://soleeh:soleeh..@localhost/gametime'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///game_time.db'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
