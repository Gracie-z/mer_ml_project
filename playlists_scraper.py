from urllib.request import urlopen
from bs4 import BeautifulSoup
import json



def save_json(url, filename):
    """
    save all playlist info from the given webpage to a json file
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

if __name__ == '__main__':
    save_json('https://open.spotify.com/genre/workout-playlists','energetic')
    save_json('https://open.spotify.com/genre/sleep-playlists','calm')
