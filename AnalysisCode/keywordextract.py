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
    custom_kw_extractor = yake.KeywordExtractor(
        lan=language,
        n=max_ngram_size,
        dedupLim=deduplication_thresold,
        dedupFunc=deduplication_algo,
        windowsSize=windowSize,
        top=numOfKeywords,
        features=None,
        stopwords=data)
    x = []
    keywords = custom_kw_extractor.extract_keywords(text)
    # print(keywords)
    # print("--------")
    for kw in keywords:
        x.append(kw[0])
    return x
