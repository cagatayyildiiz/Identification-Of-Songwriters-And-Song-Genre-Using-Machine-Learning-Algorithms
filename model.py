import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, ComplementNB
from sklearn.metrics import classification_report
import os
from sklearn import tree, svm
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectFromModel

GlobalListtoholdDataFrames=[]
path = r'C:\Users\Çağatay Yıldız\Desktop\MergedLyrics'
dirListing = os.listdir(path)                                                  # listing what is inside in the folder.
class_names=[]


def modelEstimating():
    for i in range(len(dirListing)):
        path1 = r'C:\Users\Çağatay Yıldız\Desktop\MergedLyrics\{}'.format(dirListing[i])

        dfForMergedTXT = pd.read_table(path1.replace('\u202a', ''), error_bad_lines=False)
        dfForMergedTXT.iloc[0] = [dfForMergedTXT.columns[0]]
        df_rename = {dfForMergedTXT.columns[0]: 'lyrics'}
        df_Actual = dfForMergedTXT.rename(columns=df_rename)
        Songwriter = dirListing[i][0:len(dirListing[i]) - 10]
        if Songwriter not in class_names:
            class_names.append(Songwriter)
        df_Actual['Songwriter'] = Songwriter
        if Songwriter == "Ceza" or Songwriter == "Sagopa Kajmer" or Songwriter == "Allame" or Songwriter == "Gazapizm" or Songwriter == "Ezhel" or Songwriter == "Saniser":
            df_Actual['Genre'] = "Rap"
        elif Songwriter == "Sezen Aksu" or Songwriter == "Yasar" or Songwriter == "Tarkan" or Songwriter == "KenanDogulu" or Songwriter == "Sila" or Songwriter == "MabelMatiz" or Songwriter == "SerdarOrtac":
            df_Actual['Genre'] = "Pop"
        elif Songwriter == "Duman" or Songwriter == "OgunSanlisoy" or Songwriter == "Teoman" or Songwriter == "maNga" or Songwriter == "Şebnem Ferah" or Songwriter == "Athena" or Songwriter == "Yuzyuzeyken Konusuruz":
            df_Actual['Genre'] = "Rock"
        elif Songwriter == 'Bergen' or Songwriter == "YildizTilbe" or Songwriter == "Ferdi Tayfur" or Songwriter == "Müslüm Gürses" or Songwriter == "UmitBesen" or Songwriter == "Ebru Gundes":
            df_Actual['Genre'] = "Arabesk"
        else:
            df_Actual['Genre'] = "Türk Halk Müziği"
        GlobalListtoholdDataFrames.append(df_Actual)
    df_ConcattedLyrics=pd.concat(GlobalListtoholdDataFrames)

    y = df_ConcattedLyrics['Songwriter']
    labelencoder = LabelEncoder()
    y = labelencoder.fit_transform(y)
    SongWriterList = labelencoder.classes_
    X = df_ConcattedLyrics['lyrics']
    X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.2, random_state=1234)
    X1_test=train_test_split(X, y   ,test_size=0.2, random_state=1234)

    bow_transformer_For_SongWriter=TfidfVectorizer(ngram_range=(1,2)).fit(X_train)
    text_bow_train_For_SongWriter=bow_transformer_For_SongWriter.transform(X_train)
    text_bow_test_For_SongWriter=bow_transformer_For_SongWriter.transform(X_test)





    modelForSongwriter= ComplementNB()
    modelForSongwriter = modelForSongwriter.fit(text_bow_train_For_SongWriter, y_train)




    y = df_ConcattedLyrics['Genre']
    labelencoder = LabelEncoder()
    y = labelencoder.fit_transform(y)
    GenreList=labelencoder.classes_
    X = df_ConcattedLyrics['lyrics']
    X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.2, random_state=1234)
    X1_test=train_test_split(X, y   ,test_size=0.2, random_state=1234)
    bow_transformer_For_Genre=TfidfVectorizer(ngram_range=(1,2)).fit(X_train)
    text_bow_train_For_Genre=bow_transformer_For_Genre.transform(X_train)
    text_bow_test_For_Genre=bow_transformer_For_Genre.transform(X_test)




    modelForGenre = ComplementNB()
    model = modelForGenre.fit(text_bow_train_For_Genre, y_train)




    return GlobalListtoholdDataFrames,SongWriterList,modelForSongwriter,\
           bow_transformer_For_SongWriter,modelForGenre,bow_transformer_For_Genre,GenreList




#modelEstimating('svm','none') #first parameter should be classifier name and second parameter should be feature selection method, if it is not preferred give 'none'
#modelEstimating('svm','Kbest')



