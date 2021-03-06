import os
import sys
import json
from parso import split_lines
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'cid'
secret = 'secret'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []
for i in range (0, 1000, 100):
    track_results = sp.search(q='year:2021', type='track', limit=50, offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
        

import pandas as pd

track_dataframe = pd.DataFrame({'artist_name': artist_name,
                                'track_name': track_name, 
                                'track_id': track_id,
                                'popularity': popularity
})

print(track_dataframe.shape)
print(track_dataframe.head())

track_dataframe.to_csv("playlist_" + ".csv", encoding='utf-8',index="false")