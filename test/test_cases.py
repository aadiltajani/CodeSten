"""
test file which tests all the modules
"""
from os import listdir
import sys
sys.path.append('./AnalysisCode')
from emotionanalysis import emotion_detection  # noqa: E402
from readaudio import audioinput  # noqa: E402
from speechtotext import speech_to_text  # noqa: E402
from wordcount import wordcount  # noqa: E402
from sentimentanalysis import sentiment_scores  # noqa: E402
from keywordextract import getkewords  # noqa: E402

def speechtotext(f):
    
    print("\n\nTesting speech to text conversion")
    try:
        audioinput(r"../data/test_data/"+f)
        text_dic = speech_to_text(r'../data/chunks')
        text = ''
        for i in text_dic.values():
            text += ' ' + i
        print('Speech to text:', text)
        print("Test Speech to Text passed")
    except:
        print("Test Speech to text failed")
    
    return text,text_dic

def emotionanalysis(text):
    print("\n\nTesting Emotion analysis")
    try:
        print('Emotion Analysis:', emotion_detection(text))
        print("Test Emotion analysis passed")
    except:
        print("Test Emotion Analysis failed")

def sentimentanalysis(text):
    print("\n\nTesting Sentiment analysis")
    try:
        print('Sentiment Analysis:', sentiment_scores(text))
        print("Test Sentiment analysis passed")
    except:
        print("Test Sentiment Analysis failed")

def getkeywords(text):
    print("\n\nTesting Keyword extraction")
    try:
        print('Keywords:', getkewords(text))
        print("Test Keywords extraction passed")
    except:
        print("Test Keywords extraction failed")

def testwordcount(text_dic):
    print("\n\nTesting Words count")
    try:
        print('Keywords:', wordcount(text_dic))
        print("Test Words count passed")
    except:
        print("Test Words count failed")
    
def test_all():

    for f in listdir(r"./data/test_data"):
        text,text_dic = speechtotext(f)
        emotionanalysis(text)
        sentimentanalysis(text)
        getkeywords(text)
        testwordcount(text_dic)

test_all()