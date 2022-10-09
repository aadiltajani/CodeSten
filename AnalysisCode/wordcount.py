# from speechtotext import speech_to_text


def wordcount(text_dic):
    """
    function to get word counts from the conversation
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
