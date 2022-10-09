import text2emotion as te
import nltk

# from speechtotext import speech_to_text

nltk.download('omw-1.4')


# used for emotion detection

def emotion_detection(text):
    emotionval = te.get_emotion(text)
    # print(emotionval.get('Happy'))
    # print(emotionval.get('Sad'))
    # print(emotionval)

    # need to check if there is no emotion detected
    if (emotionval.get('Happy') == 0) and (emotionval.get('Sad') == 0) and (
            emotionval.get('Fear') == 0) and (emotionval.get('Angry') == 0) \
            and (
            (emotionval.get('Surprise') == 0)):
        max_key = "No emotion detected"
        # print("yes")
    else:
        max_key = max(emotionval, key=emotionval.get)

    emotion = {'possible_emotions': emotionval, 'emotion': max_key}
    # print("emotion_detection")
    # print(emotion)
    return emotion

# text_dic = speech_to_text(r'../data/chunks')
# text = ''
# for i in text_dic.values():
#     text += ' ' + i
# print(emotion_detection(text))
