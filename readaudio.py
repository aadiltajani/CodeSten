from pydub import AudioSegment


def audioinput(file):
    a = AudioSegment.from_file(file)
    length_audio = round(len(a))
    if float(length_audio) == 0.0:
        return "Invalid Size of File"
    else:
        return "valid audio file. read successful !"


print(audioinput(r'C:\Users\asus\PycharmProjects\CodeSten\data\data_audio_agent_0002f70f7386445b.wav'))
print(audioinput(r'C:\Users\asus\PycharmProjects\CodeSten\data\data_audio_agent_0002f70f7386445b.wav'))
