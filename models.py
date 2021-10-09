from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

def connect_db(app):
    db.app = app
    db.init_app(app)
    db.drop_all
    db.create_all()

class ExampleTable(db.Model):
    __tablename__ = 'example'
    id = db.Column(db.Integer, primary_key=True)