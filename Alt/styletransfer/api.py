from flask import Flask, request, send_file
from flask_restful import Resource, Api
from neural_transfer import *

import os
import requests
import torch
import time
import sys
from torchvision import models
from torchvision import transforms


app = Flask(__name__)
api = Api(app)

class StyleTransferAPI(Resource):
	def get(self):
		style_path = "images/starry.jpg"
		content_path = "images/fox.jpg"
		resize_img(style_path)
		resize_img(content_path)
		print("Loading images", style_path, 'and', content_path)
		style_img = image_loader(style_path)
		content_img = image_loader(content_path)
		assert style_img.size() == content_img.size()

		input_img = content_img.clone()
		# input_img = torch.randn(content_img.data.size(), device=device) # For white noise
		print("Performing style transfer of", style_path, "on", content_path)
		output = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std, content_img, style_img, input_img)
		print("Style Transfer Complete! Images being displayed.")
		output_image = get_PIL(output)
		filename = content_path.split('/')[-1] + "(" + style_path.split('/')[-1] + ").jpg"
		output_path = 'outputs/' + filename
		output_image.save(output_path)
		return send_file(output_path, attachment_filename=filename)
	
	def post(self):
		content_url = request.form["content_image_url"]
		style_url = request.form["style_image_url"]
		style_path = save_image_url(style_url)
		content_path = save_image_url(content_url)
		resize_img(style_path)
		resize_img(content_path)
		style_img = image_loader(style_path)
		content_img = image_loader(content_path)
		assert style_img.size() == content_img.size()
		input_img = content_img.clone()
		# input_img = torch.randn(content_img.data.size(), device=device) # For white noise
		print("Performing style transfer of", style_path, "on", content_path)
		output = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std, content_img, style_img, input_img)
		print("Style Transfer Complete! Images being displayed.")
		output_image = get_PIL(output)
		filename = content_path.split('/')[-1] + "(" + style_path.split('/')[-1] + ").jpg"		 
		output_path = 'outputs/' + filename
		output_image.save(output_path)		
		return send_file(output_path, attachment_filename=filename)

api.add_resource(StyleTransferAPI, '/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
