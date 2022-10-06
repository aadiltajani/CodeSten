import text2emotion as te
import nltk

from speechtotext import speech_to_text_

nltk.download('omw-1.4')


# used for emotion detection

def emotion_detection(text):
    emotionval = te.get_emotion(text)
    print(emotionval.get('Happy'))
    print(emotionval.get('Sad'))
    print(emotionval)



text_dic = speech_to_text_('data/chunks')
text = ''
for i in text_dic.values():
    text += ' ' + i
print(emotion_detection(text))