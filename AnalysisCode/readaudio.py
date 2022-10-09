import shutil
from pydub import AudioSegment
import os
from pydub.utils import make_chunks
# from pathlib import Path

script_dir = os.path.dirname(__file__)
# abs path of current script needed to read audio file


def trim_audio_file(path):
    """
    function to divide audio file into smaller chunks
    to be used later for analysis
    """
    path = os.path.join(script_dir, path)
    folder_name = os.path.join(script_dir, r"../data/chunks")
    myaudio = AudioSegment.from_file(path, "wav")
    chunk_length_ms = 10000  # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms)  # Make chunk

    if os.path.isdir(folder_name):
        shutil.rmtree(folder_name)

    os.mkdir(folder_name)
    for i, chunk in enumerate(chunks):
        chunk_name = "{0}.wav".format(i)
        print("exporting", chunk_name)
        chunk.export(folder_name + "/" + chunk_name, format="wav")


def audioinput(file):
    """
    function to check and read audio file provided
    """
    if isinstance(file, str):
        file = os.path.realpath(os.path.join(script_dir, file))
    a = AudioSegment.from_file(file)
    length_audio = round(len(a))
    if float(length_audio) == 0.0:
        return "Invalid Size of File"
    else:
        print('Audio file found...dividing in chunks')
        trim_audio_file(file)
        return "Valid Audio File. Read Successful !"
