# Identification-Of-Songwriters-And-Song-Genre-Using-Machine-Learning-Algorithms

# Abstract
- Within the scope of this project, it is aimed to develop software for
determining song author and genre from lyrics using machine learning algorithms. In this context, determining the song writer and genre specific to Turkish lyrics, creating a large database of Turkish lyrics and making them available to all researchers, obtaining a native and national software for the music industry in accordance with the domestic, constitutes its innovative aspects.

- Firstly, a large database containing Turkish lyrics was created, tagged and made available to researchers within the scope of the project. Then, by using this database, songwriter and genre was determined both with conventional text classification approach and with deep learning approach. The method determined as a result of the comparative performance analysis will be implemented with an appropriate interface design.


# Results obtained by conventional Approach

|SVM             |Decision Tree                  |Naive Bayes                  |
|----------------|-------------------------------|-----------------------------|
|F1 Score= 0.56  |F1 Score = 0.44                |F1-Score = 0.57              |

- (Comparison between Classifiers in Songwriter Classification) 
- 32 Songwriters was used for this classification.

|SVM             |Decision Tree                  |Naive Bayes                  |
|----------------|-------------------------------|-----------------------------|
|F1 Score= 0.71  |F1 Score = 0.59                |F1-Score = 0.73              |

- (Comparison between Classifiers in Song Genre Classification)
- 5 Genres was used for this classification.

# Results obtained by Deep Learning Approach

|Training Time   |GPU                   |Validation Loss       |Validation Acccuracy  |Test Set Loss      |Test Set Accuracy  |F- Score           |
|----------------|----------------------|----------------------|----------------------|-------------------|-------------------|-------------------|
|66 Seconds      |Nvidia Titan RTX 24GB |1.213                 |0.378                 |2.424              |0.418              |0.39               |

- LSTM Songwriter Classification Results
- 32 Songwriters was used for this classification

|Training Time   |GPU                   |Validation Loss       |Validation Acccuracy  |Test Set Loss      |Test Set Accuracy  |F- Score           |
|----------------|----------------------|----------------------|----------------------|-------------------|-------------------|-------------------|
|135 Seconds     |Nvidia Titan RTX 24GB |1.181                 |0.6156                |1.204              |0.620              |0.62               |

- LSTM Songwriter Classification Results
- 5 Genres was used for this classification

# Conclusions 

- In conclusion, The conventional approach and deep learning methods have been built and tested. For author identification or classification (in this project case, Songwriter classification) , conventional machine learning techniques and LSTM model is compared and showed that model that trained Conventional Approach has higher accuracy. In classification problems like songwriters, It is not possible to collect big size of data. Data’s will be too short e.g. ( 20 or 30 lines for each lyric) and some songwriters does not have too many songs . For these reasons, it cannot be used Deep Learning Approach such as limited  and multi-class data.  At the end, in the scope of the project , a user interface has been implemented. 

# Dataset
- Feel free to use our dataset. 
https://drive.google.com/drive/folders/1xwA34I7rPI3crcZ8ALHxxYb03hxraQGE?usp=sharing
