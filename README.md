<p align="center"><img src="https://user-images.githubusercontent.com/112002096/194784570-00e5f8fb-0f5b-4f0c-ba4a-f0651b5b2e13.jpg" height="600px" width="auto"></img></p>

[![DOI](https://zenodo.org/badge/545685037.svg)](https://zenodo.org/badge/latestdoi/545685037)
[![workflow](https://github.com/aadiltajani/CodeSten/actions/workflows/main.yml/badge.svg)](https://github.com/aadiltajani/CodeSten/actions)
[![codecov](https://codecov.io/gh/aadiltajani/CodeSten/branch/main/graph/badge.svg?token=A4xK3vJeTW)](https://codecov.io/gh/aadiltajani/CodeSten)
[![](https://img.shields.io/badge/License-GNU-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=A020F0)](https://github.com/aadiltajani/CodeSten/blob/main/LICENSE)
![](https://img.shields.io/badge/OS-Linux-Python_informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=0000FF)
[![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=FF0000)](https://www.python.org/download/releases/3.0/)
[![](https://img.shields.io/badge/IDE-IntelliJ_IDEA-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=FFA500)](https://www.jetbrains.com/idea/)
[![](https://img.shields.io/badge/Shell-Bash-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=ffffff)](https://www.gnu.org/software/bash/)
![Lines of code](https://img.shields.io/tokei/lines/github/aadiltajani/CodeSten)
![GitHub contributors](https://img.shields.io/github/contributors/aadiltajani/CodeSten)
![GitHub language count](https://img.shields.io/github/languages/count/aadiltajani/CodeSten)
![GitHub issues](https://img.shields.io/github/issues/aadiltajani/CodeSten)
![GitHub closed issues](https://img.shields.io/github/issues-closed/aadiltajani/CodeSten)

CodeSten is Project1 for Group19 of CSC510 Software Engineering. 

CodeSten is the uncompromising stenography tool. It gives you speed, determinism, and freedom from depending upon memory or note-taking while having important conversations. You will save time and mental energy for more important matters and its completely free. Additionally, we can implement CodeSten for live audio as well as video in the coming stages. It also comes with a web GUI.


Below is a short video demonstrating the use and importance of CodeSten:


[![Watch the video](https://img.youtube.com/vi/yO7Ruh07uh8/hqdefault.jpg)](https://www.youtube.com/watch?v=yO7Ruh07uh8&ab_channel=AadilTajani)

Document Generated: https://aadiltajani.github.io/CodeSten/

# How to run

Use the package manager [ffmpeg](https://ffmpeg.org/download.html) and download the appropriate file to install the necessary package. Place the audio file in data/audiofiles folder in wav format. Mention the wav file in main.py file.

Run the following command to start the analysis of the .wav file:

Main file: [main.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/main.py)

```bash
python AnalysisCode/main.py
```

Run app.py from app folder to open the web GUI for this solution

```bash
python app/app.py
```

Pydub module uses ffmpeg to work on .wav files. After installing the package, add the bin folder path to your environment variable and you should be good to go!


# Scope
Right now it is working on audio files and any audio file can be given as input as long it is in .wav format. Just place the audio file in data/audiofiles and mention the name in [main.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/main.py)

# Requirements 
Please install all the necessary packages as mentioned in the [requirements.txt](https://github.com/aadiltajani/CodeSten/blob/main/requirements.txt) file 

# Modules Implemented
- ### Read Audio File ([readaudio.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/readaudio.py))

Function to divide audio file into smaller chunks to be used later for analysis:
```bash
def trim_audio_file(path):
```


Function to check and read audio file provided:
```bash
def audioinput(file):
```

- ### Speech to Text ([speechtotext.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/speechtotext.py))

Function to get text transcription of the audio file. It takes in path for audio chunks and uses Google's open source package speechrecognition to give us transcript of audio and it also works for multiple languages and is pretty accurate considering it is open source and free to use:
```bash
def speech_to_text(path):
```

- ### Sentiment Analysis ([sentimentanalysis.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/sentimentanalysis.py))

Function to detect speaker sentiment from positive, negative and neutral. It takes in text transcript and uses open source module to determine a sentiment for our conversation which gives us a general idea of type of conversation:
```bash
def sentiment_scores(text):
```

- ### Emotion Analysis ([emotionanalysis.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/emotionanalysis.py))

Function to detect speaker emotion There are mainly 5 emotions: happy, sad, fear, angry, and surprise. This function takes text transcript as input and uses open source package text2emotion to determine emotion from text which can be helpful in certain analysis:
```bash
def emotion_detection(text):
```

- ### Keyword Extraction ([keywordextract.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/keywordextract.py))

Function to get main keywords from the conversation This function takes all the keywords from text input and filters them by removing all the useless stopwords and gives us important keywords from the conversation and we can get imp points from the conversation:
```bash
def getkewords(text):
```

- ### Word Count ([wordcount.py](https://github.com/aadiltajani/CodeSten/blob/main/AnalysisCode/wordcount.py))

Function to get word counts from the conversation. It takes text as input and counts the number of words which can be later used to determine speech rate of speaker as low/medium/fast or for some statistical analysis:
```bash
def wordcount(text_dic):
```

# Our Dataset
Link: https://github.com/cricketclub/gridspace-stanford-harper-valley/tree/master/data/audio


# Future Work ([Link to GitHub todo list](https://github.com/users/aadiltajani/projects/1))
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


# Authors

Aadil Tajani: [Github](https://github.com/aadiltajani)

Aastha Singh: [Github](https://github.com/asingh0404)

Arpit Choudhary: [Github](https://github.com/ArpitCh21)

Dhruvish Patel: [Github](https://github.com/Dhruvish-Patel)

Kaustubh Deshpande: [Github](https://github.com/KaustubhKael)

# For Support

Dhruvish Patel: [Email](mailto:dhruvishpatel02@gmail.com)

Aadil Tajani: [Email](mailto:tajani.aadil@gmail.com)
