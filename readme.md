# **End-to-End Sentiment Analysis and Deployment of Amazon Fine Food Reviews**

## **Overview**

This project presents a complete machine learning pipeline for analyzing customer sentiments from the **Amazon Fine Food Reviews** dataset. It covers data preprocessing, feature extraction, model training, evaluation, deployment via Flask API, and containerization with Docker. The trained model predicts whether a review expresses **positive** or **negative** sentiment, providing practical insights for businesses and consumers.

---

## **Table of Contents**

1. [Dataset](#dataset)
2. [Project Workflow](#project-workflow)
3. [Model Development](#model-development)
4. [Flask Application](#flask-application)
5. [Frontend Integration](#frontend-integration)
6. [Dockerization](#dockerization)
7. [Project Structure](#project-structure)
8. [Installation and Usage](#installation-and-usage)
9. [Results](#results)
10. [Future Enhancements](#future-enhancements)

---

## **Dataset**

* **Source:** [Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews/data)
* **Size:** 568,454 reviews
* **Columns:**
  `Id`, `ProductId`, `UserId`, `ProfileName`, `HelpfulnessNumerator`, `HelpfulnessDenominator`, `Score`, `Time`, `Summary`, `Text`

The dataset contains customer reviews of fine foods from Amazon. Each review includes text data and a numerical rating (1–5). Reviews with ratings ≥ 4 are considered **positive**, and those ≤ 2 are **negative** for binary classification.

---

## **Project Workflow**

1. **Data Preprocessing**

   * Loaded and cleaned raw dataset.
   * Removed duplicates and missing values.
   * Selected relevant columns (`Score`, `Text`).
   * Converted text to lowercase, removed punctuation, stopwords, and special characters.
   * Transformed target variable into binary labels.

2. **Feature Extraction**

   * Used **TF-IDF Vectorization** to convert text data into numerical features.

3. **Model Building & Evaluation**

   * Algorithms used: Logistic Regression, Support Vector Machine (SVM), Random Forest, Gradient Boosting.
   * Evaluated models using Accuracy, Precision, Recall, F1-Score, ROC-AUC, and Confusion Matrix.
   * Selected the best-performing model based on overall performance metrics.

4. **Model Saving**

   * Serialized trained model and vectorizer using `pickle`:

     * `sentiment_model.pkl`
     * `tfidf_vectorizer.pkl`

5. **Application Development**

   * Built a **Flask API** (`app.py`) to serve real-time predictions.
   * Added endpoints:

     * `/` – Home route.
     * `/predict` – Accepts JSON input and returns predicted sentiment.

6. **Frontend Integration**

   * Developed a responsive **HTML, CSS, and JS** interface.
   * Allows users to input a review and view sentiment predictions instantly.

7. **Dockerization**

   * Created a Dockerfile for consistent deployment.
   * Built and ran the containerized Flask app for portability.

---

## **Model Development**

**Libraries Used:**

* `pandas`, `numpy`
* `scikit-learn`
* `flask`, `flask-cors`
* `pickle`

**Key Steps:**

* Data cleaning and binary label encoding
* TF-IDF vectorization
* Training multiple models
* Saving the best model and vectorizer

---

## **Flask Application**

The Flask app serves as the backend API that loads the saved model and vectorizer, processes user input, and returns predictions in JSON format.

Example Request:

```bash
POST /predict
{
  "text": "The product quality was excellent and delivery was fast."
}
```

Example Response:

```json
{
  "sentiment": "Positive",
  "confidence": 92.35
}
```

---

## **Frontend Integration**

**Features:**

* Clean and modern user interface.
* Responsive layout with gradient theme.
* AJAX-based communication with Flask API.
* Displays both sentiment and confidence score dynamically.

---

## **Dockerization**

**Dockerfile:**

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask flask-cors scikit-learn numpy pandas
EXPOSE 5000
CMD ["python", "app.py"]
```

**Commands:**

```bash
docker build -t sentiment-analyzer .
docker run -p 5000:5000 sentiment-analyzer
```

The application will be available at:
**[http://localhost:5000](http://localhost:5000)**

---

## **Project Structure**

```
sentiment-analysis/
│
├── app.py
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── Dockerfile
├── requirements.txt
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── index.html
│
└── README.md
```

---

## **Installation and Usage**

1. **Clone Repository**

   ```bash
   git clone <repo-url>
   cd sentiment-analysis
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Flask App**

   ```bash
   python app.py
   ```

4. **Access**
   Open browser → [http://localhost:5000](http://localhost:5000)

---

## **Results**

* Best Model: **Logistic Regression**
* Accuracy: ~90%
* The deployed Flask application successfully predicts sentiments in real-time.
* Dockerization ensures consistent deployment across environments.

---

## **Future Enhancements**

* Add multi-class classification (positive, neutral, negative).
* Integrate deep learning models like LSTM or BERT.
* Deploy to cloud (AWS, Render, or Azure).
* Implement user feedback and sentiment trend dashboard.

