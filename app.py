from flask import Flask, redirect, url_for, render_template, request
import model

app = Flask(__name__)

GlobalList,SongWriterList,ServerModelForSongwriter,BowTransformerForSongwriter,ServerModelForGenre,\
BowTransformerForGenre,GenreList=model.modelEstimating()

SongwriterLink={'Allame' : "https://www.youtube.com/embed/6vHxhaK9qL4?list=PLrdC_uHJ6z6e7wHLmBJWV6dqFb4ucGTl-",
                'Arif Sağ':'https://www.youtube.com/embed/K__qZo0ykT8?list=PL4LnHqnyuhroddzNZ55VnouuwXBxiBIu-',
                'Aşık Veysel':'https://www.youtube.com/embed/EkpON4m61w4?list=PLVh3yCU50cWnX0ZO8_RUsAVMxX2Y9HJV-',
                'Athena': 'https://www.youtube.com/embed/Z8aqzdARZns',
                'Bergen' : 'https://www.youtube.com/embed/Diq85zNtJlw?list=PLJs9MI3Ki7gNdsI021whRZL0BIEU36asx',
                'Ceza' : 'https://www.youtube.com/embed/4AWJBMawRZk',
                'Duman': 'https://www.youtube.com/embed/3bfkyXtuIXk?list=PLqcCBunO7lOlQTrt66kD1bXzL97QOa4hz',
                'Ebru Gündeş':'https://www.youtube.com/embed/-XKi5PAAFp8?list=PLiX80h37csslXy1s2caatyhibqiEFNbma',
                'Ezhel':'https://www.youtube.com/embed/o-OPeZIELHE',
                'Ferdi Tayfur':'https://www.youtube.com/embed/d0YYMdXMfS0?list=PLnUzviUPq9_ybJ4p61CWcnj7PJqn6hd1h',
                'Gazapizm':'https://www.youtube.com/embed/BcjoGIoErdE',
                'Kenan Doğulu':'https://www.youtube.com/embed/EOrM5Qe21JU',
                'Mabel Matiz':'https://www.youtube.com/embed/ME1WaoCudmw',
                'Musa Eroğlu':'https://www.youtube.com/embed/fHGV2Rsh0Pc',
                'Müslüm Gürses':'https://www.youtube.com/embed/lYNMQBKDhwg?list=PLoUHqJk21ZW5iFNFrZAfioQWhVRf-eIBI',
                'Neşet Ertaş':'https://www.youtube.com/embed/7yQI2mUX7Rc',
                'Ogün Şanlısoy':'https://www.youtube.com/embed/3YL4Btzcf2Q',
                'Orhan Hakalmaz':'https://www.youtube.com/embed/4kTU-LgMgws',
                'Sagopa Kajmer':'https://www.youtube.com/embed/PUiNB0UFwJM',
                'Şanışer':'https://www.youtube.com/embed/L5K3IxINr7A',
                'Selda Bağcan':'https://www.youtube.com/embed/ATxRhKHVX7k',
                'Serdar Ortaç':'https://www.youtube.com/embed/Ze0-2_GmzWk',
                'Sezen Aksu':'https://www.youtube.com/embed/D-i77gTIEWM',
                'Sıla':'https://www.youtube.com/embed/kXBunIe_PSw',
                'Tarkan':'https://www.youtube.com/embed/U66ixhdbxEI',
                'Teoman':'https://www.youtube.com/embed/Sdw7eaCSzhg',
                'Ümit Besen':'https://www.youtube.com/embed/DcgPCU10Bek',
                'Yaşar':'https://www.youtube.com/embed/qpAeILUvIJQ',
                'Yıldız Tilbe':'https://www.youtube.com/embed/V2-9oGCC-eE',
                'Yüzyüzeyken Konuşuruz':'https://www.youtube.com/embed/2ZI3XjHNM1s',
                'maNga':'https://www.youtube.com/embed/fZYZPANBF6g',
                'Şebnem Ferah':'https://www.youtube.com/embed/IqbZGfWV-Io'}




giveLink=""

@app.route("/")
def home():
    return render_template("HomePage.html",len=len(SongWriterList) , Songwriters=SongWriterList)

@app.route("/prediction", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        Lyric = request.form["nm"]
        LearningMethod=request.form["options"]
        LyricArray = Lyric.split(" ")
        FixedLyric=""
        for i in range(len(LyricArray)):
            if LyricArray[i]!=" " or LyricArray[i]!="":
                FixedLyric=FixedLyric+" "+LyricArray[i][:5]
        PredictedSongWriter= GlobalList[
            ServerModelForSongwriter.predict(
                BowTransformerForSongwriter.transform([FixedLyric]))[0]].iloc[0][
            'Songwriter']
        PredictedGenre= GenreList[ServerModelForGenre.predict(
            BowTransformerForGenre.transform([FixedLyric]))][0]
        giveLink=SongwriterLink[str(PredictedSongWriter)]
        return render_template("Second Page.html",len=len(SongWriterList) , Songwriters=SongWriterList,Songwriter = PredictedSongWriter,genre=PredictedGenre,SongwriterLink=giveLink)
    else:
        return render_template("Second Page.html",len=len(SongWriterList),Songwriters=SongWriterList,Songwriter = "PredictedSongWriter",genre="PredictedGenre",SongwriterLink="giveLink")

@app.route("/<usr>")
def user(usr):
    return render_template('Second Page.html')

if __name__ == "__main__":
    app.run(debug=True)
