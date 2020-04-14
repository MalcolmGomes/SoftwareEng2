import requests
from imgurpython import ImgurClient as imgurclient

client_id = 'a16a7a11c249975'
client_secret = '42476db137960713495783563ddeb29890dd159b'

client = imgurclient(client_id, client_secret)
imgurclient.upload_from_path('./fox.jpg', config=None, anon=True)