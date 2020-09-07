import pandas as pd
import os
GlobalListtoholdDataFrames=[]
path = r'C:\Users\Çağatay Yıldız\Desktop\MergedLyrics'
dirListing= os.listdir(path)

class_names=[]
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
        if Songwriter=="Ceza" or Songwriter=="Sagopa Kajmer" or Songwriter=="Allame" or Songwriter=="Gazapizm" or Songwriter=="Ezhel" or Songwriter=="Saniser":
            df_Actual['Genre'] = "rap"
        elif Songwriter=="Sezen Aksu" or Songwriter=="Yasar" or Songwriter=="Tarkan"or Songwriter=="KenanDogulu" or Songwriter=="Sila" or Songwriter=="MabelMatiz" or Songwriter=="SerdarOrtac":
            df_Actual['Genre'] = "pop"
        elif Songwriter=="Duman" or Songwriter=="OgunSanlisoy" or Songwriter=="Teoman"or Songwriter=="maNga" or Songwriter=="Şebnem Ferah"or Songwriter=="Athena" or Songwriter=="Yuzyuzeyken Konusuruz":
            df_Actual['Genre'] = "rock"
        elif Songwriter=='Bergen' or Songwriter=="YildizTilbe" or Songwriter=="Ferdi Tayfur" or Songwriter=="Müslüm Gürses"or Songwriter=="UmitBesen" or Songwriter=="Ebru Gundes":
            df_Actual['Genre'] = "Arabesk"
        else:
            df_Actual['Genre']="TurkHalkMuzigi"
        GlobalListtoholdDataFrames.append(df_Actual)

df_ConcattedLyrics=pd.concat(GlobalListtoholdDataFrames)

aggregation_functions = {'Songwriter':'first', 'lyrics': 'sum'}
df_new = df_ConcattedLyrics.groupby('Songwriter').aggregate(aggregation_functions)
newdf=df_new['lyrics']

newdataframe=pd.DataFrame()
for i in range( newdf.size ):
    newdataframe[class_names[i]]=newdf[i]
print ("dfasfds")