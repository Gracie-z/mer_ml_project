import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display
from numpy.lib.npyio import save


def save_spectogram_waveplot(song_id):
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

if __name__ == '__main__':
    save_spectogram_waveplot('0BCUve4b3KySD9Sk8CMZ2i')