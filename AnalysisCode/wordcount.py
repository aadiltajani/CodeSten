# from speechtotext import speech_to_text


def wordcount(text_dic):
    number_of_words_1 = 0
    countval = 0
    for i in text_dic.values():
        word_list = i.split()
        number_of_words = len(word_list)
        countval += number_of_words
    # print(countval)
    return countval


# text_dic = speech_to_text_]('data/chunks')
# print(wordcount(text_dic))