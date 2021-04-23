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


pl_id = 'spotify:playlist:37i9dQZF1DWXML2LendtLJ'
offset = 0


response = sp.playlist_items(pl_id,
                                offset=offset,
                                fields='items.track.uri,total',
                                additional_types=['track'])
print('response: ', response)
tids = [item['track']['uri'] for item in response['items']]

    

features = sp.audio_features(tids)

fieldnames = ['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature']
import csv
with open('data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for feature in features:
        track = {key:feature[key] for key in fieldnames}
        print('track: ',track)
        writer.writerow(track)


