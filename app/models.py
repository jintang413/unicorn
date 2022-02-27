from datetime import datetime
from app import db
import enum


class MenuItemType(enum.Enum):
    STARTER = 'Starter'
    ENTREE = 'Entree'
    DESSERT = 'Dessert'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    type = db.Column(db.Enum(MenuItemType))
    description = db.Column(db.String(140))
    vegetarian = db.Column(db.Boolean())

    def __repr__(self):
        return f'<Menu {self.name}>\n{self.description}'