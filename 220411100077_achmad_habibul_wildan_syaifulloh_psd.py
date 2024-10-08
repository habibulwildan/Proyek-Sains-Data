# -*- coding: utf-8 -*-
"""220411100077_Achmad Habibul Wildan Syaifulloh_PSD.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1arOkKGMKgKrHtVHD0qBKZQCdUSeI55b6
"""

import pandas as pd

# Membaca file CSV dan mengubahnya menjadi kerangka data (dataframe)
# Ganti 'file.csv' dengan path file CSV yang ingin Anda baca
df = pd.read_csv('/content/cobak.csv')

# Menampilkan 5 baris pertama dari dataframe
print(df.head())

#Target encoding
import pandas as pd
df['Target'] = [1,0,1,0,1,0,1]
mean_target = df.groupby('Merek')['Stok'].mean()
df['Merek'] = df['Merek'].map(mean_target)
print(df)

datakategori= df['Merek']
print(datakategori)

#label encoding
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
numeric_data = label_encoder.fit_transform(datakategori)
print(numeric_data)

