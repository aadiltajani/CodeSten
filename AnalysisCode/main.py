# import sys
# sys.path.append('../')
from emotionanalysis import emotion_detection
from readaudio import audioinput
from speechtotext import speech_to_text

print(audioinput(r"../data/audiofiles/data_audio_agent_0002f70f7386445b.wav"))
text_dic = speech_to_text(r'../data/chunks')
print('\nSpeech to text:',text_dic)

text = ''
for i in text_dic.values():
    text += ' ' + i
print(emotion_detection(text))