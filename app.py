from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

# Load the trained model and TF-IDF vectorizer
with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# Home route - serve frontend
@app.route('/')
def home():
    return app.send_static_file('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get('text', '')
        if not text.strip():
            return jsonify({'error': 'No text provided'}), 400

        text_tfidf = tfidf.transform([text])
        prediction = model.predict(text_tfidf)[0]
        sentiment = 'Positive' if prediction == 1 else 'Negative'
        return jsonify({'sentiment': sentiment})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
