# importing required libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem import WordNetLemmatizer
import re
import copy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def imp_data(convert):
  # importing the dataset
  sentiment_data = pd.read_csv('Tweets-Copy1.csv')

  # Dropping year collumn because all have the same year
  sentiment_df = sentiment_data.drop(sentiment_data[sentiment_data['airline_sentiment_confidence']<0.5].index, axis= 0)

  # Assigning collumns to X and Y
  X = sentiment_df['text']
  Y = sentiment_df['airline_sentiment']

  # Cleaning our text data:
  nltk.download('stopwords')

  lemmatizer = WordNetLemmatizer()
  stop_words = stopwords.words('english')
  punctuations = string.punctuation
  nltk.download('wordnet')

  clean_data = []
  for i in range(len(X)):
    text = re.sub('[^a-zA-Z]', ' ',X.iloc[i])
    text = text.lower().split()
    text = [lemmatizer.lemmatize(word) for word in text if (word not in stop_words) and (word not in punctuations)]
    text = ' '.join(text)
    clean_data.append(text)

  # Adding the input to the dataset
  input_data = [convert]
  input_data1 = copy.deepcopy(clean_data)
  input_data.extend(input_data1)

  # Making the model
  count_vectorizer = CountVectorizer(max_features = 5000, stop_words = ['virginamerica','united'])
  X_input_fit = count_vectorizer.fit_transform(input_data).toarray()

  count_vectorizer = CountVectorizer(max_features = 5000, stop_words = ['virginamerica','united'])
  X_fit = count_vectorizer.fit_transform(clean_data).toarray()

  # print(([X_input_fit[0]]*5000)[100])
  # print(([X_input_fit[0]]*5000)[200])
  # print(([X_input_fit[0]]*5000)[100][0])
  # print(([X_input_fit[0]]*5000)[200][0])
  model = MultinomialNB()

  # Making testing data and training data
  X_train, X_test, Y_train, Y_test = train_test_split(X_fit,Y, test_size = 0.3)
  model.fit(X_train,Y_train)

  y_pred = model.predict(X_test)

  # Getting the classification report
  classification = classification_report(Y_test,y_pred)
  print(classification)

  # Printing the sentiment of the model
  y_input_pred = model.predict(X_input_fit)
  return y_input_pred
