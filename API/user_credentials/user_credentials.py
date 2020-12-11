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
    custID = db.Column(db.Integer, primary_key=True)
    #public id will be seen when decoded, so make it different from the id cause then itll be harder for people to figure out the users in the database
    public_id = db.Column(db.String(50), unique=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    nric = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer(3))
    phoneNumber = db.Column(db.String(10))
    email = db.Column(db.String(80))
    address = db.Column(db.String(80))

app.route('/user', methods=['GET'])
@token_required
def get_all_users():

    users = User.query.all()

    output = [] #need to generate a new list first because cannot output sqlalchemy results into a json object directly

    for user in users:
        user_data = {} #create new dictionary for each user
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password #it will be hashed 
        user_data['admin'] = user.admin
        output.append(user_data)    

    return jsonify({'users' : output})