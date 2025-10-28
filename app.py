from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

@app.route('/')
def home():
    return "✅ Flask Sentiment Analysis API is running. Use POST /predict to test."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    text_tfidf = tfidf.transform([text])
    prediction = model.predict(text_tfidf)[0]
    sentiment = 'Positive' if prediction == 1 else 'Negative'
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
