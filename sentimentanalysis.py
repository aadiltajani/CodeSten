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

