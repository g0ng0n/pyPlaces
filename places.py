from flask import Flask, render_template
from flask import request, redirect, jsonify, url_for, flash
import json
from flask import make_response
import random
import string

app = Flask(__name__)


# API END POINTS
@app.route('/api/v1/places')
def showAllPlaceJSON():
    # We get all the places from the json

    with open('places.json') as json_data:
        d = json.load(json_data)
        print(d)


    print (d)
    if d:
        return jsonify(d)
    else:
        response = make_response(json.dumps('Places Not Found.'), 404)
        response.headers['Content-Type'] = 'application/json'
        return response

# API END POINTS
@app.route('/api/v1/places/<int:place_id>')
def showPlaceJSON():
    # We get all the places from the json PLaces
    place = ""
    if place:
        return jsonify(Place=place)
    else:
        response = make_response(json.dumps('Place Not Found.'), 404)
        response.headers['Content-Type'] = 'application/json'
        return response


if __name__ == '__main__':
    app.secret_key = 'secreto_magico'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
