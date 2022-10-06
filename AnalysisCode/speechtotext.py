import os
import speech_recognition as sr

r = sr.Recognizer()


def speech_to_text_(path):
    with open(path, "rb") as f:
        with sr.AudioFile(f) as source:
            audio_listened = r.record(source)
            # try converting it to text
            text = r.recognize_google(audio_listened, language='en-Us')
    return text


script_dir = os.path.dirname(__file__)  # abs path of current script needed to read audio file
print(speech_to_text_(os.path.join(script_dir, r"../data/audiofiles/data_audio_agent_0002f70f7386445b.wav")))
