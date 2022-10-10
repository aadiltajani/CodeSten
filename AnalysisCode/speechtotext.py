# __author__      = "Aadil Tajani, Dhruvish Patel, Kaustubh Deshpande, Aastha Singh, Arpit Chaudhary"
# __copyright__      = "Open source libraries"
import os
import speech_recognition as sr
r = sr.Recognizer()
script_dir = os.path.dirname(__file__)
# abs path of current script needed to read audio file


def speech_to_text(path):
    """
    function to get text transcription of the audio file.
    It takes in path for audio chunks and uses Google's
    open source package
    speechrecognition to give us transcript of audio and it
    also works for multiple languages and is pretty accurate
    considering it is open source and free to use.
    """
    path = os.path.join(script_dir, path)
    finaltext = {}
    arr = os.listdir(path)
    for x in arr:
        xpath = os.path.join(path, x)
        with open(xpath, "rb") as f:
            with sr.AudioFile(f) as source:
                audio_listened = r.record(source)
                # try converting it to text
                try:
                    text = r.recognize_google(audio_listened, language='en-Us')
                # handling error if speech recognizer
                # can't work on it (empty audio)
                except sr.UnknownValueError:
                    # print("Error:", str(e))
                    finaltext[x] = ""
                else:
                    text = f"{text.capitalize()}. "
                    finaltext[x] = text
    return finaltext


# print(speech_to_text_(os.path.join(script_dir, r"..\data\chunks")))
