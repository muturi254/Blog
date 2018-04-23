from . import db 
from flask_login import UserMixin

from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
# user model
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    # setting table users
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(255), unique = True, index=True)

class PlogPost(db.Model):

    __tablename__ = 'post'
    # setting table post
    id = db.Column(db.Integer, primary_key=True)
