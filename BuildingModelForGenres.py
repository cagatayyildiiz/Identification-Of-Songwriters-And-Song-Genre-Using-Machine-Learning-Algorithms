import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, ComplementNB
from sklearn.metrics import classification_report
from sklearn.metrics import plot_roc_curve

import os
from sklearn import tree, svm
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import confusion_matrix

GlobalListtoholdDataFrames=[]
path = r'C:\Users\Çağatay Yıldız\Desktop\MergedLyrics'
dirListing = os.listdir(path)
GenresWithSongwriters = {
  "rap": ["Allame","Ceza","Ezhel","Gazapizm","Sagopa Kajmer"],
}


for i in range(len(dirListing)):
    path1 = r'C:\Users\Çağatay Yıldız\Desktop\MergedLyrics\{}'.format(dirListing[i])

    dfForMergedTXT=pd.read_table(path1.replace('\u202a',''),error_bad_lines=False)
    dfForMergedTXT.iloc[0] = [dfForMergedTXT.columns[0]]
    df_rename = {dfForMergedTXT.columns[0]:'lyrics'}
    df_Actual=dfForMergedTXT.rename(columns=df_rename)
    Songwriter=dirListing[i][0:len(dirListing[i])-10]
    df_Actual['Songwriter']=Songwriter
    df_Actual['Genre']=

    GlobalListtoholdDataFrames.append(df_Actual)

df_ConcattedLyrics=pd.concat(GlobalListtoholdDataFrames)

y = df_ConcattedLyrics['Songwriter']
labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y)

X = df_ConcattedLyrics['lyrics']
X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.2, random_state=1234)
X1_test=train_test_split(X, y   ,test_size=0.1, random_state=1234)
bow_transformer=TfidfVectorizer().fit(X_train)
text_bow_train=bow_transformer.transform(X_train)
text_bow_test=bow_transformer.transform(X_test)
model=svm.SVC()
FeatureSelection="L1"
if FeatureSelection=='none':
    model = model.fit(text_bow_train, y_train)
    print(text_bow_test.shape)
    print(text_bow_train.shape)
    # getting the predictions of the Validation Set...
    predictions = model.predict(text_bow_test)
    # getting the Precision, Recall, F1-Score
    print(classification_report(y_test, predictions))
    print(GlobalListtoholdDataFrames[model.predict(bow_transformer.transform(["Dolun çok seviy"]))[0]].iloc[0]['Songwriter'])
elif FeatureSelection=='L1':
    lsvc = LinearSVC(C=10 ,penalty="l1", dual=False,max_iter=120000).fit(text_bow_train, X_train)
    modelxx = SelectFromModel(lsvc, prefit=True)
    NewTrainBow = modelxx.transform(text_bow_train)
    print(NewTrainBow.shape)
    NewTestBow= modelxx.transform(text_bow_test)
    print(NewTestBow.shape)
    model = model.fit(NewTrainBow, y_train)
    predictions = model.predict(NewTestBow)
    print(classification_report(y_test, predictions))
    print(GlobalListtoholdDataFrames[
              model.predict(modelxx.transform(bow_transformer.transform(["Bi' de kafam bass vurur ama yine yok"])))[0]].iloc[0][
              'Songwriter'])
    print(confusion_matrix(y_test,predictions))
    svc_disp = plot_roc_curve(model, X_test, y_test)
elif FeatureSelection=='Kbest':
    NewTrainBow = SelectKBest(chi2, k=2500).fit_transform(text_bow_train, y_train)
    NewTestBow = SelectKBest(chi2, k=2500).fit_transform(text_bow_test, y_test)
    model = model.fit(NewTrainBow, y_train)
    predictions = model.predict(NewTestBow)
    print(classification_report(y_test, predictions))
    print(GlobalListtoholdDataFrames[
              model.predict(bow_transformer.transform(["Bi' de kafam bass vurur ama yine yok"]))[0]].iloc[0][
              'Songwriter'])




#modelEstimating('svm','none') #first parameter should be classifier name and second parameter should be feature selection method, if it is not preferred give 'none'
#modelEstimating('svm','L1')
#modelEstimating('svm','Kbest')



