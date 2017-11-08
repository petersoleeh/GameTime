from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    pass_secure = db.Column(db.String(255))
    favourite = db.relationship("Favourite", backref="user", lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return  {self.username}

class Match:
    '''
    match class to define match objects
    '''

    def __init__(self,home,home_id,away,away_id,date):
        self.home=home
        self.home_id=home_id
        self.away=away
        self.away_id=away_id
        self.date=date

class League:
    '''
    league class to define the standings
    '''
    def __init__(self,pos,team,team_id,points,played,gd):
        self.pos=pos
        self.team=team
        self.team_id=team_id
        self.points=points
        self.played=played
        self.gd=gd

class Favourite(db.Model):
    __tablename__ = 'favourites'

    id = db.Column(db.Integer,primary_key = True)
    team_id= db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))



    @classmethod
    def add_favorites(self,cls):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_favourites(self,cls):
        db.session.delete(self)
        db.session.commit()
