import sys
sys.path.append('./')
from AnalysisCode.readaudio import audioinput
from AnalysisCode.speechtotext import speech_to_text_

print(audioinput(r"../data/audiofiles/data_audio_agent_0002f70f7386445b.wav"))
print('\nSpeech to text:',speech_to_text_(r"../data/chunks"))