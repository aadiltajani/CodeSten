# import all the libraries and packages
import traceback
import nltk
from speechtotext import speech_to_text_

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(text):
    if len(text) == 0:
        sentiment_ = ""
    else:
        sid_obj = SentimentIntensityAnalyzer()
        sentiment_dict = sid_obj.polarity_scores(text)
        del sentiment_dict['compound']  # we dont need compound sentiment value
        max_key = max(sentiment_dict, key=sentiment_dict.get)
        print(max_key)

        if max_key == "neu":
            sentiment = "Neutral"
        elif max_key == "pos":
            sentiment = "Positive"
