# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
from pprint import pprint

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False
binary_labels = {'sad': -1, 'calm': -1, 'happy': 1, 'energetic': 1}
multiclass_labels = {'sad': 1, 'calm': 2, 'happy': 3, 'energetic': 4}

def get_features_and_label(pl_id, label):

    pl_id = 'spotify:playlist:' + pl_id
    # sample: spotify:playlist:37i9dQZF1DWXML2LendtLJ'
    offset = 0


    response = sp.playlist_items(pl_id,
                                    offset=offset,
                                    fields='items.track.uri,items.track.name,items.track.artists.name,items.track.preview_url,total')

    tids = [item['track']['uri'] for item in response['items']]
    info = [{'artist_name':item['track']['artists'][0]['name'], 'track_name':item['track']['name'], 'preview_url':item['track']['preview_url']} for item in response['items']]


        

    features = sp.audio_features(tids)
    fieldnames = ['id','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature','artist_name','track_name','preview_url']

    import csv
    with open('data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames + ['binary_label', 'multiclass_label'])
        writer.writeheader()
        for feature,info in zip(features, info):
            feature.update(info)
            track = {key:feature[key] for key in fieldnames}
            track['binary_label'] = binary_labels[label]
            track['multiclass_label'] = multiclass_labels[label]
            writer.writerow(track)


