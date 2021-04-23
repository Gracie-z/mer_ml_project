from urllib.request import urlopen
import pandas as pd
import os


df = pd.read_csv('data.csv',usecols=['id','preview_url'], keep_default_na=False)


for index, id, url in df.itertuples():
    if not url:
        continue
    print(url)
    print(type(url))
    html = urlopen(url)
    file_dir = os.path.join('audio',id+'.wav')
    print(file_dir)
    with open(file_dir, 'wb') as f:
        f.write(html.read())