from flask import Flask
from flask import render_template
import json
from travel_spider_class import TravelSpider
app=Flask(__name__)

@app.route('/')
def index():
	travel=TravelSpider()
	data=travel.get_data()
	return render_template('map.html', name=json.dumps(data))

if __name__=='__main__':
	app.run()
