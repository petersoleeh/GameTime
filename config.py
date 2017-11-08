import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://soleeh:soleeh..@localhost/gametime'
    GAME_WEEK_API='http://127.0.0.1:3000/teams/week/12'
    TEAM_URL='http://127.0.0.1:3000/teams/{}'

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
