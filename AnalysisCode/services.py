
from CodeSten import open_source
import librosa
import datetime
from Analysis import silence_detection
import logging
from Analysis import query_ES
logging.basicConfig(filename="logfileanalysis.log",  
               format='%(asctime)s %(message)s',  
               filemode='a')  
