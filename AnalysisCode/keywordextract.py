import yake
from yake.highlight import TextHighlighter

from speechtotext import speech_to_text_

with open("data\stopwordlist\stopwords_en.txt", "r") as file:
    data = file.read()
    data = data.lower().split('\n')

# from Analysis import stopwords
def getkewords(text):
    language = "en"
    max_ngram_size = 2
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 35
