from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid #to generate random public id
from werkzeug.security import generate_password_hash, check_password_hash #want the passwords to be hashed 
import jwt
import datetime
from functools import wraps

