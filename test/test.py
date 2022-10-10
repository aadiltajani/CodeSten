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

print("Testing all functions on different test audios...")
for f in listdir(r"./data/test_data"):
    try :
        audioinput(r"../data/test_data/"+f)
        text_dic = speech_to_text(r'../data/chunks')
        text = ''
        for i in text_dic.values():
            text += ' ' + i    
        print("\n\nTesting speech to text conversion")
        print('Speech to text:', text)
        print("Speech to text conversion successful")
        print("\n\nTesting Emotion analysis")
        print('Emotion Analysis:', emotion_detection(text))
        print("Emotion analysis successful")
        print("\n\nTesting Sentiment analysis")
        print('Sentiment Analysis:', sentiment_scores(text))
        print("Sentiment analysis successful")
        print("\n\nTesting Keywords extraction")
        print('Keywords:', getkewords(text))
        print("Keywords extraction successful")
        print("\n\nTesting words count")
        print('Word count:', wordcount(text_dic))
        print("Words count successful\n\n")
    except:
        print("Testing failed")