from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

@app.route('/')
def home():
    return "✅ Amazon Fine Food Reviews Sentiment API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        review = data.get("review", "")

        if not review:
            return jsonify({"error": "No review text provided."}), 400

        text_vector = vectorizer.transform([review])
        prediction = model.predict(text_vector)[0]
        sentiment = "Positive" if prediction == 1 else "Negative"

        return jsonify({"review": review, "sentiment": sentiment})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
