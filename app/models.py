from app import db
from app import login
from flask_login import  UserMixin
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore, Security
from datetime import date, datetime
from werkzeug.security import generate_password_hash, check_password_hash




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(255))
    location = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=True)
    created_on = db.Column(db.DateTime, default=date.today())
    # roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    status=db.Column(db.String(55),default='normal')
    products=db.relationship('Product',backref='dealer',lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)




@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# userdatastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, userdatastore)
