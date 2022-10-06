from pydub import AudioSegment
import os

script_dir = os.path.dirname(__file__)  # abs path of current script needed to read audio file


def audioinput(file):
    a = AudioSegment.from_file(file)
    length_audio = round(len(a))
    if float(length_audio) == 0.0:
        return "Invalid Size of File"
    else:
        return "valid audio file. read successful !"


print(audioinput(os.path.join(script_dir, r"data\audiofiles\data_audio_agent_0002f70f7386445b.wav")))
print(audioinput(os.path.join(script_dir, r"data\audiofiles\data_audio_caller_0002f70f7386445b.wav")))
