# __author__      =
# "Aadil Tajani, Dhruvish Patel,
# Kaustubh Deshpande, Aastha Singh, Arpit Chaudhary"
# __copyright__      = "Open source libraries"
import yake
# from yake.highlight import TextHighlighter
import os
# from speechtotext import speech_to_text_

with open(os.path.join(os.path.dirname(__file__),
                       r"../data/stopwordlist/stopwords_en.txt"), "r") as file:
    data = file.read()
    data = data.lower().split('\n')


# from Analysis import stopwords
def getkewords(text):
    """
    function to get main keywords from the conversation
    This function takes all the keywords from text input
    and filters them by removing all the useless
    stopwords and gives us important keywords
    from the conversation and we can get imp
    points from the conversation
    """
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

# text_dic = speech_to_text_('data/chunks')
# text = ''
# for i in text_dic.values():
#     text += ' ' + i
# print(getkewords(text))
