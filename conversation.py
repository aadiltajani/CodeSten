from pydub import AudioSegment
from pydub.utils import make_chunks
import os
import speech_recognition as sr
r = sr.Recognizer()
import logging
logging.basicConfig(filename="logfileanalysis.log",  
               format='%(asctime)s %(message)s',  
               filemode='a') 



def trim_audio_file(path, folder_name):
    logger.info("trim_audio_file in conversationpy")
    myaudio = AudioSegment.from_file(path, "wav")
    chunk_length_ms = 59000  # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms)  # Make chunk
    #folder_name = name
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    for i, chunk in enumerate(chunks):
        chunk_name = "{0}.wav".format(i)
        # print("exporting", chunk_name)
        chunk.export(folder_name + "/"+ chunk_name, format="wav")

