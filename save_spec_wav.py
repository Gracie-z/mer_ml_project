import matplotlib.pyplot as plt
import csv
#for loading and visualizing audio files
import librosa
import librosa.display
import numpy as np

from urllib.request import urlopen
import pandas as pd
import os


def get_wav(csvfile):
    df = pd.read_csv(csvfile,usecols=['id','preview_url'], keep_default_na=False)
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


def main(filename, name):
    
    df = pd.read_csv(filename, usecols=['id'])
    for index, id in df.itertuples():
        if len(id) < 10:
            continue
        i = index // 300
        wav_file = f'audio/{name}/{id}.wav'
        x, sr = librosa.load(wav_file, sr=100)
        x = np.append(x,id)
        with open(f'data_csv/{name}{i}_vectors.csv','a') as f:
            writer = csv.writer(f)
            writer.writerow(x)
            print(index,id,x)


def save_spectogram_waveplot(song_id):
    """
    song_id: str:: unique spotify id of a song
    """

    filename = 'audio/' + song_id + '.wav'
    x, sr = librosa.load(filename, sr=44100)

    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)
    plt.savefig('spectogram/' + song_id + '.png')

    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.savefig('waveplot/' + song_id + '.png')


# save all spectograms and waveplots from a csv to a directory
import pandas as pd

def save_graphs(csvfile):
    """
    input: str:: a csvfile that stores info about the url of the songs
    """
    df = pd.read_csv(csvfile,usecols=['id','preview_url'])
    df.dropna(inplace=True)

    for index, id, url in df.itertuples():
        save_spectogram_waveplot(id)



def generate_graphs(csvfile):
    """
    csvfile: str
    automatically save all spectograms and waveplots of all the songs listed in the csvfile
    """
    get_wav(csvfile)
    save_graphs(csvfile)


if __name__ == '__main__':
    main('data_csv/sad_no_duplicates_no_nan.csv','sad')