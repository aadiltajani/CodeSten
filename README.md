<p align="center"><img src="https://user-images.githubusercontent.com/112002096/194784570-00e5f8fb-0f5b-4f0c-ba4a-f0651b5b2e13.jpg" height="600px" width="auto"></img></p>

[![DOI](https://zenodo.org/badge/545685037.svg)](https://zenodo.org/badge/latestdoi/545685037)
[![workflow](https://github.com/aadiltajani/CodeSten/actions/workflows/main.yml/badge.svg)](https://github.com/aadiltajani/CodeSten/actions)
[![codecov](https://codecov.io/gh/aadiltajani/CodeSten/branch/main/graph/badge.svg?token=A4xK3vJeTW)](https://codecov.io/gh/aadiltajani/CodeSten)
[![](https://img.shields.io/badge/License-MIT-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)](https://github.com/aadiltajani/CodeSten/blob/main/LICENSE)
![](https://img.shields.io/badge/OS-Linux-Python_informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
[![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)](https://www.python.org/download/releases/3.0/)
[![](https://img.shields.io/badge/IDE-IntelliJ_IDEA-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)](https://www.jetbrains.com/idea/)
[![](https://img.shields.io/badge/Shell-Bash-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)](https://www.gnu.org/software/bash/)

CodeSten is Project1 for Group19 of CSC510 Software Engineering. 

CodeSten is the uncompromising stenography tool. It gives you speed, determinism, and freedom from depending upon memory or note-taking while having important conversations. You will save time and mental energy for more important matters.

Below is a short video demonstrating the use and importance of CodeSten:


[![Watch the video](https://img.youtube.com/vi/yO7Ruh07uh8/hqdefault.jpg)](https://www.youtube.com/watch?v=yO7Ruh07uh8&ab_channel=AadilTajani)

Document Generated: https://aadiltajani.github.io/CodeSten/


# How to run
Main file: [main.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/main.py)
python AnalysisCode/main.py 
or can be seen on github actions

# Scope
Right now it is working on audio files and any audio file can be given as input as long it is in .wav format. Just place the audio file in data/audiofiles and mention the name in .... function


# Modules Implemented
- Read Audio File ([readaudio.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/readaudio.py))
- Speech to Text ([speechtotext.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/speechtotext.py))
- Sentiment Analysis ([sentimentanalysis.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/sentimentanalysis.py))
- Emotion Analysis ([emotionanalysis.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/emotionanalysis.py))
- Keyword Extraction ([keywordextract.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/keywordextract.py))
- Word Count ([wordcount.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/wordcount.py))

# Our Dataset: 
Link: https://github.com/cricketclub/gridspace-stanford-harper-valley/tree/master/data/audio


# Requirements:
Listed in Requirements.txt


# Future Work: 
- Implement Video emotion analysis and combine with audio analysis done here
- Silence detection
- Determine Speech Rate of speaker (slow, medium, fast)
- Match the accuracy of current solution with the transcript provided in dataset listed above
- Give transcript with time stamp and merge transcripts of both sides to show a converstaion in text
- Do it for live audio/video file
- Added graphs and more functionalities on website/GUI of choice
- Allow multiple files to be worked upon simultaneously by implementing multiple workers
- Using GCP, AWS and IBM services to test open source results and compare accuracy
- Make discord bots/APIs to use this functionality as a service anywhere.
- Implement scoring conversation based on keyword spotting and filtering conversation
