import json
import bottle
from bottle import route, run, request, abort
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime

connection = MongoClient('localhost', 27017)
db = connection.yourdatabase




@route('/')
def home():
    return ['hello, world']


@route('/restaurants', method='GET')
def say_hello():
    return "Hello from /restaurant"


# Retrieve all data in JSON format
@route('/wifi/getall', method='GET')
def get_all_restaurant():
    entity = db.wifi.find()
    if not entity:
        abort(404, 'No restaurant with id %s' % id)
    return dumps(entity)


# Call this to drop all data after retrieving
@route('/restaurants/dropall', method='GET')
def drop_all_restaurant():
    db.restaurants.drop()
    return "ALL DATA DROPPED"


# Retrieve data be unique id. Probably not gonna use it here.
@route('/restaurants/:id', method='GET')
def get_restaurant_with_id(id):
    entity = db['restaurants'].find_one({'_id':id})
    if not entity:
        abort(404, 'No restaurant with id %s' % id)
    return dumps(entity)


# Run the server and listen to all interface on port 8080
run(host='0.0.0.0', port=8080, reloader=True)
