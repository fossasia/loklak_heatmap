# -*- coding: iso-8859-15 -
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json
import requests

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/search')
def search():
	query = request.args.get('q')
	url = "http://loklak.org/api/search.json?q="+query
	locations = []
	json_data = requests.get(url).json()
	tweets = json_data['statuses']
	for t in tweets :
		if 'location_mark' in t.keys():
			locations.append(t['location_mark'])
	return json.dumps(locations)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
