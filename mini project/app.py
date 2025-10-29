from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
        color = "green"
    elif polarity < 0:
        sentiment = "Negative 😞"
        color = "red"
    else:
        sentiment = "Neutral 😐"
        color = "gray"

    return render_template('result.html', text=text, sentiment=sentiment, color=color, polarity=polarity)

if __name__ == '__main__':
    app.run(debug=True)
