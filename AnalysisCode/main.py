# import sys
# sys.path.append('../')
from readaudio import audioinput
from speechtotext import speech_to_text_

print(audioinput("Data/audiofiles/data_audio_agent_0002f70f7386445b.wav"))
print('\nSpeech to text:',speech_to_text_("/Data\/chunks"))