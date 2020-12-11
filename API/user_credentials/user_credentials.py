from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid #to generate random public id
from werkzeug.security import generate_password_hash, check_password_hash #want the passwords to be hashed 
import jwt
import datetime
from functools import wraps
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
#create a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./local.db'

db = SQLAlchemy(app)

class User(db.Model):
    custID = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    nric = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer(3))
    phoneNumber = db.Column(db.String(10))
    email = db.Column(db.String(80))
    address = db.Column(db.String(80))

@app.route('/user', methods=['GET'])
def get_all_users():

    users = User.query.all()

    output = [] #need to generate a new list first because cannot output sqlalchemy results into a json object directly

    for user in users:
        user_data = {} #create new dictionary for each user
        user_data['custID'] = user.custID
        user_data['firstname'] = user.firstname
        user_data['lastname'] = user.lastname
        user_data['nric'] = user.nric
        user_data['gender'] = user.gender
        user_data['age'] = user.age
        user_data['phoneNumber'] = user.phoneNumber
        user_data['email'] = user.email
        user_data['address'] = user.address
        output.append(user_data)    

    return jsonify({'users' : output})

