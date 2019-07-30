import pickle
import sklearn
from flask import Flask, jsonify, make_response, request
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

app = Flask(__name__)
# Load model
model = joblib.load('house_predict.pkl')

@app.route('/score', methods=['POST'])
def score():
    # Input/API request containing the features to predict on. 
    # As an production requirement, ensure that you validate an API key in the header before proceeding.
    features = request.json['X']
    prediction = model.predict([features])
    if len(prediction)>0:
        return make_response(jsonify({'prediction': prediction[0], 'timestamp':datetime.now()}))
    else:
        return make_response(jsonify({'prediction': None, 'timestamp':datetime.now()}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)