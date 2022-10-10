# import all the libraries and packages
# import traceback
import nltk
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# from speechtotext import speech_to_text

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))


def sentiment_scores(text):
    """
    function to detect speaker sentiment from positive, negative and neutral.
    It takes in text transcript and uses open source module to determine
    a sentiment for our conversation which gives us a general idea of
    type of conversation
    """
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
        else:
            sentiment = "Negative"
        sentiment_ = {}
        sentiment_['possible_sentiment'] = sentiment_dict
        sentiment_['sentiment'] = sentiment
        sentiment_ = {}
        sentiment_['possible_sentiment'] = sentiment_dict
        sentiment_['sentiment'] = sentiment
    return sentiment_
