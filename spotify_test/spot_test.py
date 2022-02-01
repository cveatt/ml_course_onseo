import os
import sys
import json
import numpy as np
import pandas as pd
from parso import split_lines
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

credentials = json.load(open('spotify_test/author.json'))
client_id = credentials['client_id']
client_secret = credentials['client_secret']

playlist_index = 0

playlists = json.load(open('spotify_test/playlist_like_or_dislike.json'))
playlist_uri = playlists[playlist_index]['uri']
like = playlists[playlist_index]['like']

client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = playlist_uri
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]


results = sp.user_playlist(username, playlist_id, 'tracks')


playlist_tracks_data = results['tracks']
playlist_tracks_id = []
playlist_tracks_titles = []
playlist_tracks_artists = []

for track in playlist_tracks_data['items']:
    playlist_tracks_id.append(track['track']['id'])
    playlist_tracks_titles.append(track['track']['name'])


    artist_list = []
    for artist in track['track']['artists']:
        artist_list.append(artist['name'])
    playlist_tracks_artists.append(artist_list)
    
    features = sp.audio_features(playlist_tracks_id)


features_df = pd.DataFrame(data=features, columns=features[0].keys())
features_df['title'] = playlist_tracks_titles
features_df['album_id'] = features_df['album'].apply(lambda x: x['name'])
features_df['album_release_date'] = features_df['album'].apply(lambda x: x['release_date'])
features_df['all_artists'] = playlist_tracks_artists

#features_df = features_df.set_index('id')
features_df = features_df[['id', 'title', 'popularity', 'type', 'all_artists', 'album_id', 'album_name',
                           'danceability', 'energy', 'key', 'loudness',
                           'mode', 'acousticness', 'instrumentalness',
                           'liveness', 'valence', 'tempo',
                           'duration_ms', 'time_signature']]
features_df.tail()
features_df.to_csv("playlist_1" + str(playlist_index) + ".csv", encoding='utf-8',index="false")