from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open(r'C:\\Users\\Brajesh Mohapatra\\Python\\Bike Count Prediction\\bike_count_prediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        hour = int(request.form['Time'])
        temperature = float(request.form['Temperature in °C'])
        workingday = request.form['Working Day']
        if workingday == 'No':
            workingday = 0
        else:
            workingday = 1
        humidity = float(request.form['Humidity'])
        season = request.form['Season']
        if season == 'Spring':
            season = 1
        elif season == 'Summer':
            season = 2
        elif season == 'Autumn':
            season = 3
        else:
            season = 4
        entries = np.array([hour, temperature, workingday, humidity, season])
        entries = entries.reshape(1, -1)
        prediction = model.predict(entries)
        prediction = (prediction) ** 3
        prediction = prediction.round(decimals = 0)
        output = prediction[0]
        return render_template('index.html', prediction_text = "Predicted Number of Bikes is {}".format(output))
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)        