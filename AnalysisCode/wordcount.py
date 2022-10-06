def wordcount(text_dic):

    countval = 0
    for i in text_dic.values():
        number_of_words = len(i)
        countval += number_of_words

    print(countval)
    return countval


text_dict = {1: 'This', 2: 'is', 3: 'Earth'}
x = wordcount(text_dict)