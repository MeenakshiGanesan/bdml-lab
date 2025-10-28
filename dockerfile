FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask flask-cors scikit-learn numpy pandas

EXPOSE 5000

CMD ["python", "app.py"]
