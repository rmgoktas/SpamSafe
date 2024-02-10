from flask import Flask, request, jsonify
import joblib
import requests

app = Flask(__name__)

#load model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # get text
    text = request.json['text']

    # vectorize text
    text_vectorized = vectorizer.transform([text])

    # predict
    prediction = model.predict(text_vectorized)

    # return predict value to client
    if prediction == 1:
        return jsonify({'result': 'SPAM'})
    elif prediction == 2:
        return jsonify({'result': 'Normal'})
    else:
        return jsonify({'result': 'Prediction error.'})

if __name__ == '__main__':
    app.run(debug=True)
