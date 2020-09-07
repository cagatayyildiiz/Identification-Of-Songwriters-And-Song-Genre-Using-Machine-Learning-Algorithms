import os
import function as function
path = r'C:\Users\Çağatay Yıldız\Desktop\ProcessedDataSet'                                                                # getting path for lyrics

dirListing = os.listdir(path)                                                  # listing what is inside in the folder.

stopwordsPath = r'C:\Users\Çağatay Yıldız\Desktop\stopwords.txt'                                    # getting path for stopwords

readStop = open(stopwordsPath, "r", encoding='utf-8')

stopwords = readStop.readlines()

for y in range(len(dirListing)):
    pathType = path+"\\"+dirListing[y]                                # in dirlisting we have folders like ceza, sagopa
    dirListing2 = os.listdir(pathType)                                # in dirlisting2 we have folders like lyricsceza1

    for x in range(len(dirListing2)):
        SongWPath = r'C:\Users\Çağatay Yıldız\Desktop\ProcessedDataSet\{}\{}'.format(dirListing[y], dirListing2[x])          # getting  a SongWriter path
        dirListing3 = os.listdir(SongWPath)

        # Open file3 in write mode
        saveFilePath="C:\\Users\\Çağatay Yıldız\\Desktop\\MergedLyrics\\"+dirListing2[x]+"Merged.txt".lstrip('\u202a')

        with open(saveFilePath, 'a', encoding='utf-8') as outfile:

            # Iterate through list
            for names in dirListing3:
                # Open each file in read mode
                with open(SongWPath+"\\"+names, "r", encoding='utf-8') as infile:
                    # read the data from file1 and
                    # file2 and write it in file3
                    # infile.readlines()
                    outfile.write(infile.read())

                    # Add '\n' to enter data of file2
                # from next line
                outfile.write("\n")

        """ file3 = open(stopwordsPath, "r", encoding="utf-8")                    # ?
        stopwords = file3.readlines()

        writeSameFile = open(lyricPath, 'w', encoding='utf-8')                # Write Stemming in same file
        n = writeSameFile.write(function.listToString(allStr))
        writeSameFile.close()"""