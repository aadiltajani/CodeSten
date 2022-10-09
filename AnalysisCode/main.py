"""
main file which calls all the modules
"""
import sys
sys.path.append('./AnalysisCode')
from emotionanalysis import emotion_detection  # noqa: E402
from readaudio import audioinput  # noqa: E402
from speechtotext import speech_to_text  # noqa: E402
from wordcount import wordcount  # noqa: E402
from sentimentanalysis import sentiment_scores  # noqa: E402
from keywordextract import getkewords  # noqa: E402

print(audioinput(r"../data/audiofiles/data_audio_agent_0002f70f7386445b.wav"))
text_dic = speech_to_text(r'../data/chunks')

text = ''
for i in text_dic.values():
    text += ' ' + i
print('\nSpeech to text:', text)
print('\nEmotion Analysis:', emotion_detection(text))
print('\nSentiment Analysis:', sentiment_scores(text))
print('\nKeywords:', getkewords(text))
print('\nWord count:', wordcount(text_dic))
