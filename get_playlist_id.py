import json
import csv


def get_song_id(type):
    with open('playlists/' + type + '.json',) as f:
        info = json.load(f)
    content = info['content']
    items = content['items']
    with open('playlists/' + type + '.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['playlist_id'])
        writer.writeheader()
        for item in items:
            print(item['id'])
            writer.writerow({'playlist_id':item['id']})


if __name__ == '__main__':
    get_song_id('energetic')
    get_song_id('calm')


