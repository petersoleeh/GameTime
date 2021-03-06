import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://soleeh:soleeh..@localhost/gametime'
    GAME_WEEK_API='https://gtime-api.herokuapp.com/teams/week/12'
    TEAM_URL='https://gtime-api.herokuapp.com//teams/{}'
    LEAGUE_URL='https://gtime-api.herokuapp.com//teams/league/{}'
    SEARCH_URL='https://gtime-api.herokuapp.com//teams/search/{}'

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


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
