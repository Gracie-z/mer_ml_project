from save_features_labels import get_features_and_label
import pandas as pd

def main_calm_energetic():
    calm_df = pd.read_csv('playlists/calm.csv')
    energetic_df =  pd.read_csv('playlists/energetic.csv')
    
    for index, id in calm_df.itertuples():
        print(index,id)
        get_features_and_label(id,'calm')

    for index, id in energetic_df.itertuples():
        get_features_and_label(id,'energetic')

def sad_and_happy():
    sad_df = pd.read_csv('playlists/sad.txt')
    happy_df = pd.read_csv('playlists/happy.txt')
    for index, id in sad_df.itertuples():
        print(index,id)
        get_features_and_label(id,'sad')

    for index, id in happy_df.itertuples():
        print(index,id)
        get_features_and_label(id,'happy')




    
if __name__ == '__main__':
    sad_and_happy()