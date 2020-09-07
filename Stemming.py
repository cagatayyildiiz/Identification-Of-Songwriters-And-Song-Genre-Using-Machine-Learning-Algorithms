import function as function
import os, os.path

path = r'C:\Users\Çağatay Yıldız\Desktop\ProcessedDataSet'                                                           # getting path for lyrics

dirListing = os.listdir(path)                                                  # listing what is inside in the folder.

stopwordsPath = r'C:\Users\Çağatay Yıldız\Desktop\stopwords.txt'                                    # getting path for stopwords

readStop = open(stopwordsPath, "r", encoding='utf-8')

stopwords = readStop.readlines()

for j in range(len(stopwords)):                                                # removing \n 's from stopwords
    stopwords[j] = stopwords[j].replace('\n', "")

for y in range(len(dirListing)):
    pathType = path+"\\"+dirListing[y]                                # in dirlisting we have folders like ceza, sagopa
    dirListing2 = os.listdir(pathType)                                # in dirlisting2 we have folders like lyricsceza1

    for x in range(len(dirListing2)):
        SongWPath = r'C:\Users\Çağatay Yıldız\Desktop\ProcessedDataSet\{}\{}'.format(dirListing[y], dirListing2[x])          # getting  a SongWriter path
        dirListing3 = os.listdir(SongWPath)

        for h in range(len(dirListing3)):
            lyricPath = SongWPath + "\\" + dirListing3[h]
            lyricText = open(lyricPath, "r", encoding='utf-8')                         # getting a Lyric path
            allStr = lyricText.readlines()

            for i in range(len(allStr)):
                temp = allStr[i].lower().split(' ')                                             # splitting a line of a lyric

                for a in range(len(temp)):

                    for k in range(len(stopwords)):                                               # removing stopwords
                        if temp[a].__contains__(stopwords[k]):
                            temp[a] = ""
                    if (temp[a].__contains__("\n") and len(temp[a]) >= 4):
                        temp[a] = temp[a].replace('(', '').replace(')','').replace('"',"").replace('.','').replace(',',"").replace("[","").replace("]","") # removing punctions , ( ) is exist on data but no . or ,
                        temp[a] = temp[a] + " "
                        temp[a] = temp[a][:5] + "\n"
                    else:
                        temp[a] = temp[a].replace('(', '').replace(')','').replace('"',"").replace('.','').replace(',',"").replace("[","").replace("]","")  # removing punctions , ( ) is exist on data but no . or ,
                        temp[a] = temp[a][:5] + " "

                allStr[i] = function.listToString(temp)

            lyricText.close()

            file3 = open(stopwordsPath, "r", encoding="utf-8")                    # ?
            stopwords = file3.readlines()

            writeSameFile = open(lyricPath, 'w', encoding='utf-8')                # Write Stemming in same file
            n = writeSameFile.write(function.listToString(allStr).replace("\n\n",""))
            writeSameFile.close()





