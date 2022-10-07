# import all the libraries and packages
import traceback
import nltk
# from speechtotext import speech_to_text

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
        else:
            sentiment = "Negative"
        sentiment_ = {}
        sentiment_['possible_sentiment'] = sentiment_dict
        sentiment_['sentiment'] = sentiment
        sentiment_ = {}
        sentiment_['possible_sentiment'] = sentiment_dict
        sentiment_['sentiment'] = sentiment
    return sentiment_

# print(sentiment_scores("The Google Cloud Natural Language API can be used to reveal the structure and meaning 
# of text via powerful machine learning models. You can use it to extract information about people, places, 
# events and much more, mentioned in text documents, news articles or blog posts. You can use it to understand sentiment about 
# your product on social media or parse intent from customer conversations happening in a call center or a messaging app. 
# You can analyze text uploaded in your request or integrate with your document storage on Google Cloud Storage."))
