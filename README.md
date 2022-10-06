# CodeSten
[![DOI](https://zenodo.org/badge/545685037.svg)](https://zenodo.org/badge/latestdoi/545685037)
[![workflow](https://github.com/aadiltajani/CodeSten/actions/workflows/main.yml/badge.svg)](https://github.com/aadiltajani/CodeSten/actions)


CodeSten is Project1 for Group19 of CSC510 Software Engineering
# Description


# Why to Use


# How to run
python AnalysisCode/main.py 
or can be seen on github actions

# Scope
Right now it is working on audio files and any audio file can be given as input as long it is in .wav format. Just place the audio file in data/audiofiles and mention the name in .... function


# Modules Implemented
- Read Audio File ([readaudio.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/readaudio.py))
- Speech to Text (speechtotext.py)
- Sentiment Analysis (sentimentanalysis.py)
- Emotion Analysis (emotionanalysis.py)
- Keyword Extraction
- Word Count

# Our Dataset: 
Link: https://github.com/cricketclub/gridspace-stanford-harper-valley/tree/master/data/audio


# Requirements:
Listed in Requirements.txt





# Future Work: 
- Implement Video emotion analysis and combine with audio analysis done here
- Silence detection
- Match the accuracy of current solution with the transcript provided in dataset listed above
- Give transcript with time stamp and merge transcripts of both sides to show a converstaion in text
- Do it for live audio/video file
- Added graphs and more functionalities on website/GUI of choice
- Allow multiple files to be worked upon simultaneously by implementing multiple workers
- Using GCP, AWS and IBM services to test open source results and compare accuracy
- Make discord bots/APIs to use this functionality as a service anywhere.
- Implement scoring conversation based on keyword spotting and filtering conversation
