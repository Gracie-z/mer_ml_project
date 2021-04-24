from urllib.request import urlopen
from bs4 import BeautifulSoup
import json



def save_json(url, filename):
    """
    save all playlist info from the given webpage to a json file
    only necessary for calm/energetic
    """
    html = urlopen(url)
    html_filename = 'playlists/' + filename + '.html'
    with open(html_filename, 'wb') as f:
        f.write(html.read())
    with open(html_filename, 'rb') as f:
        html = f.read()

    bs = BeautifulSoup(html, 'html.parser')
    script = bs.body.find_all('script')
    info = str(script[2]) # this adds unexpected blackslashes ??!
    print(script) 


    with open('playlists/'+filename+'.json','wb') as f:
        json.dump(info,f)


import csv


def get_playlist_id(type):
    """
    type: str:: calm/energetic
    given json, get all playlist ids
    """
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
    save_json('https://open.spotify.com/genre/workout-playlists','energetic')
    save_json('https://open.spotify.com/genre/sleep-playlists','calm')
    get_playlist_id('energetic')
    get_playlist_id('calm')






