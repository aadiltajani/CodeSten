from pydub import AudioSegment
from pydub.utils import make_chunks
import os
import speech_recognition as sr
r = sr.Recognizer()
import logging
logging.basicConfig(filename="logfileanalysis.log",  
               format='%(asctime)s %(message)s',  
               filemode='a')  
