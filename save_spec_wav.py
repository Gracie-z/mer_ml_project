from plot_spec_wav import save_spectogram_waveplot as save
import pandas as pd

df = pd.read_csv('data.csv',usecols=['id','preview_url'])
df.dropna(inplace=True)

for index, id, url in df.itertuples():
    save(id)