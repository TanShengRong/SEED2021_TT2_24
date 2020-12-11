from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid #to generate random public id
from werkzeug.security import generate_password_hash, check_password_hash #want the passwords to be hashed 
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
#create a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./local.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #public id will be seen when decoded, so make it different from the id cause then itll be harder for people to figure out the users in the database
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean) #will be true or false, whether they are admin or not 