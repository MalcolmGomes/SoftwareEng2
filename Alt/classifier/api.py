from flask import Flask, request
from flask_restful import Resource, Api
from classifier import *

import os
import requests
import torch
import time
import sys
from torchvision import models
from torchvision import transforms


app = Flask(__name__)
api = Api(app)

class ClassificationAPI(Resource):
	def get(self):
		img = Image.open("malcolm.jpg")
		inference, confidence, duration = classify(img)
		return {
			'inference': inference,
			'confidence': confidence,
			'duration': duration
		}
	
	def post(self):
		image_url = request.form["image_url"]
		filename = image_url.split('/')[-1]
		r = requests.get(image_url, allow_redirects=True)
		open(filename, 'wb').write(r.content)           
		img = Image.open(filename)          
		inference, confidence, duration = classify(img)
		os.remove(filename)
		return {
			'inference': inference,
			'confidence': confidence,
			'duration': duration
		}

api.add_resource(ClassificationAPI, '/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
