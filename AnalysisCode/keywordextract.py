import yake
from yake.highlight import TextHighlighter

from speechtotext import speech_to_text_

with open("data\stopwordlist\stopwords_en.txt", "r") as file:
    data = file.read()
    data = data.lower().split('\n')
