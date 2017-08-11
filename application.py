from flask import (Flask, render_template, request, redirect, jsonify, url_for,
                   flash)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Part, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///computerhw.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog')
def showCategories():
    categories = session.query(Category).order_by(asc(Category.name))
    return render_template('publiccategories.html', categories=categories)


@app.route('/catalog/<int:category_id>/')
def showParts(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    """creator = getUserInfo(category.user_id)"""
    parts = session.query(Part).filter_by(category_id=category_id).all()
    return render_template('publicparts.html', parts=parts, category=category)
    

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
