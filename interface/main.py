import requests
import json
import cv2
from PIL import Image
# Command Line Interface for Containerized Deep Learning Models (Q/q to quit program)
print('Command Line Interface for Containerized Deep Learning Models (Q/q to quit program)')

def listModels(models):
    i = 0 
    for model in models:
        i+=1
        print(str(i) + ':', model)

models = ['Classification (c)', 'Saliency Mapper (s)', 'Style Transfer(t)']
listModels(models)
while True:
    input_value = input('Enter an image URL (q to quit): ')
    if input_value.isalpha(): 
        val = input_value.lower()
        if val == 'q': break
    image_url = input_value
    input_value = input('Choose model (q to quit): ')
    if input_value.isalpha(): 
        val = input_value.lower()
        if val == 'q': break
        elif val == 'c': 
            api_url = 'http://localhost:5001'
            response = requests.post(api_url, data = {"image_url": image_url})
            print(response.text)
        elif val == 's':
            api_url = 'http://localhost:5002'
            response = requests.post(api_url, data = {"image_url": image_url})
            filename = image_url.split('/')[-1]
            open('outputs/(SaliencyMap) ' + filename, 'wb').write(response.content)    
            print('Saliency map of ', filename, 'saved in images.')
        elif val == 't':
            style_image_url = input('Enter a style image URL (q to quit): ')
            api_url = 'http://localhost:5003'
            response = requests.post(api_url, data = {"style_image_url": style_image_url, "content_image_url": image_url})
            filename = image_url.split('/')[-1] + " (" + style_image_url.split('/')[-1] + ").jpg"
            open('outputs/(StyleTransfer) ' + filename, 'wb').write(response.content)    
            print('Style Transfer', filename, 'saved in images.')
            
            
    
            
print('Exiting interface program.')