import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.callbacks import EarlyStopping
from keras.layers import Dropout
import re
from nltk import word_tokenize
from bs4 import BeautifulSoup
from IPython.core.interactiveshell import InteractiveShell
import plotly.figure_factory as ff
from keras.models import load_model
InteractiveShell.ast_node_interactivity = 'all'
from plotly.offline import iplot
import os
path = r'C:\Users\Çağatay Yıldız\Desktop\MergedLyrics'
dirListing= os.listdir(path)
GlobalListtoholdDataFrames=[]
class_names=[]
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def GetModel(FixedLyric):

    for i in range(len(dirListing)):
            path1 = r'C:\Users\Çağatay Yıldız\Desktop\MergedLyrics\{}'.format(dirListing[i])

            dfForMergedTXT=pd.read_table(path1.replace('\u202a',''),error_bad_lines=False)
            dfForMergedTXT.iloc[0] = [dfForMergedTXT.columns[0]]
            df_rename = {dfForMergedTXT.columns[0]:'lyrics'}
            df_Actual=dfForMergedTXT.rename(columns=df_rename)
            Songwriter=dirListing[i][0:len(dirListing[i])-10]
            if Songwriter not in class_names:
                class_names.append(Songwriter)
            df_Actual['Songwriter']=Songwriter
            if Songwriter=="Ceza" or Songwriter=="Sagopa Kajmer" or Songwriter=="Allame" or Songwriter=="Gazapizm" or Songwriter=="Ezhel":
                df_Actual['Genre'] = "rap"
            elif Songwriter=="Sezen Aksu" or Songwriter=="Yasar" or Songwriter=="Tarkan"or Songwriter=="KenanDogulu" or Songwriter=="Sila":
                df_Actual['Genre'] = "pop"
            elif Songwriter=="Duman" or Songwriter=="OgunSanlisoy" or Songwriter=="Teoman"or Songwriter=="maNga" or Songwriter=="Şebnem Ferah"or Songwriter=="Athena" or Songwriter=="Yuzyuzeyken Konusuruz":
                df_Actual['Genre'] = "rock"
            elif Songwriter=="Asik Veysel" or Songwriter=="Musa Eroglu" or Songwriter=="Neset Ertas":
                df_Actual['Genre'] = "TurkHalkMuzigi"
            elif Songwriter=='Bergen' or Songwriter=="YildizTilbe" or Songwriter=="Ferdi Tayfur" or Songwriter=="Müslüm Gürses"or Songwriter=="UmitBesen":
                df_Actual['Genre'] = "Arabesk"
            else:
                df_Actual['Genre']="TurkSanatMuzigi"
            GlobalListtoholdDataFrames.append(df_Actual)
    df_ConcattedLyrics=pd.concat(GlobalListtoholdDataFrames)
    dfs = pd.read_csv('Dataset.csv')
    dfs['lyrics'] = dfs['lyrics'].astype(str)
    dfs['lyrics'] = dfs['lyrics'].str.replace('\d+', '')

    MAX_NB_WORDS = 16870
    # Max number of words in each complaint.
    MAX_SEQUENCE_LENGTH = 150
    # This is fixed.
    EMBEDDING_DIM = 125
    tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
    tokenizer.fit_on_texts(dfs['lyrics'])
    word_index = tokenizer.word_index

    X = tokenizer.texts_to_sequences(dfs['lyrics'])
    X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
    Y = pd.get_dummies(df_ConcattedLyrics['Genre']).values

    model = load_model('GenreModel.h5')


    new_song = [FixedLyric]
    seq = tokenizer.texts_to_sequences(new_song)
    padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
    pred = model.predict(padded)
    classes_list=dfs['Genre'].unique()


    return classes_list[np.argmax(pred)]



