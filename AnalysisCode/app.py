from fileinput import filename
from flask import Flask, render_template, request
from emotionanalysis import emotion_detection
from readaudio import audioinput
from speechtotext import speech_to_text
from wordcount import wordcount


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analysis',methods=['POST'])
def analysis():
    input =  request.files['inp']
    
    # print(input)
    
    # output = model.predict(input)
    # output = round(output[0],3)
    ans = audioinput(r'../data/audiofiles/'+input.filename)
    # ans = audioinput(input)
    text_dic = speech_to_text(r'../data/chunks')
    ans = ans + "<br><br>"
    ans = ans + '<br>Speech to text:' + str(text_dic)

    text = ''
    for i in text_dic.values():
        text += ' ' + i
    ans = ans + "<br><br>" + str(emotion_detection(text))

    ans = ans + "<br><br>" + 'word count:' +  str(wordcount(text_dic))
    # return render_template('index.html')

    # return render_template('index.html', analysis_text = 'Weight should be {}lbs.'.format(output))
    print(ans)
    return render_template('index.html', analysis_text = ans)

if __name__ == "__main__":
    app.run(debug=True)