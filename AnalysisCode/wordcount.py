# __author__      = "Aadil Tajani, Dhruvish Patel, Kaustubh Deshpande, Aastha Singh, Arpit Chaudhary"
# __copyright__      = "Open source libraries"

def wordcount(text_dic):
    """
    function to get word counts from the conversation. It takes text
    as input and counts the number of words which can be later used to
    determine speech rate of speaker as low/medium/fast or for some
    statistical analysis.
    """
    countval = 0
    for i in text_dic.values():
        word_list = i.split()
        number_of_words = len(word_list)
        countval += number_of_words
    # print(countval)
    return countval


# text_dic = speech_to_text_]('data/chunks')
# print(wordcount(text_dic))
