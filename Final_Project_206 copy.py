import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import urllib3
import facebook
import requests

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Drake'

client_id = "b4742e4596f04490a340dbbceeeed1b7"
client_secret = "90a54c8916674e77bd84add7183a8d9c"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

result = sp.search(search_str)

access_token= 'EAAY2RBMZBQFcBAPF464p45qgZAxC4HfM4gHyJNN5Y8MLhdIjTWKfPhg2sb3hKSKcV8LXA9fWrxeenZC77GZCEEemvZCalxg4H1m1qr4f7ZBt4gcsxyuZCZAb11eAhGxUmrreBAlJUnhaINZA0r70sPUHZA6qdvjYPzZAo0ZD'


r = requests.get('https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id=123&client_secret=XXX')
access_token = r.text.split[1]
print (access_token)