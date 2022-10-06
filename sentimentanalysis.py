# import all the libraries and packages
import traceback
import nltk
from speechtotext import speech_to_text_

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

