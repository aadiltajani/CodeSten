import text2emotion as te
import nltk

# from speechtotext import speech_to_text

nltk.download('omw-1.4')


# used for emotion detection

def emotion_detection(text):
    """
    function to detect speaker emotion
    """
    emotionval = te.get_emotion(text)
    # print(emotionval.get('Happy'))
    # print(emotionval.get('Sad'))
    # print(emotionval)

    # need to check if there is no emotion detected

    if (emotionval.get('Happy') == 0) and (emotionval.get('Sad') == 0) and (
            emotionval.get('Fear') == 0) and (emotionval.get('Angry') == 0) \
            and (
            (emotionval.get('Surprise') == 0)):
        """
        check if emotion is detected and output accordingly
        """
        max_key = "No emotion detected"
    else:
        max_key = max(emotionval, key=emotionval.get)
    emotion = {'possible_emotions': emotionval, 'emotion': max_key}
    """
    output all percentage of emotion values and
    the final detected emotion as well
    """
    # print("emotion_detection")
    # print(emotion)
    return emotion
