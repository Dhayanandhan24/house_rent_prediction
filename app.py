# flask w/ model ML
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

model = joblib.load('modelJoblib')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ml')
def ml():
    medinc = 4.240700
    houseage = 40
    averooms = 5.694362
    avebedrms = 1.032641
    population = 1851
    aveoccup = 2.746291
    latitude = 34.16
    longitude = -117.99
    hasil = model.predict([[
        medinc, houseage, averooms, avebedrms, population,
        aveoccup, latitude, longitude 
    ]])[0]
    return str(hasil)

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        body = request.json
        # 8 vars
        medinc = body['medinc']
        houseage = body['houseage']
        averooms = body['averooms']
        avebedrms = body['avebedrms']
        population = body['population']
        aveoccup = body['aveoccup']
        latitude = body['latitude']
        longitude = body['longitude']
        # model prediction
        hasil = model.predict([[
            medinc, houseage, averooms, avebedrms, population,
            aveoccup, latitude, longitude 
        ]])[0]
        return jsonify({
            'medinc' : body['medinc'],
            'houseage' : body['houseage'],
            'averooms' : body['averooms'],
            'avebedrms' : body['avebedrms'],
            'population' : body['population'],
            'aveoccup' : body['aveoccup'],
            'latitude' : body['latitude'],
            'longitude' : body['longitude'],
            'PRICE_PREDICTION' : hasil,
            'status': 'sukses POST'
        })
    elif request.method == 'GET':
        return jsonify({
            'status': 'Anda nge-GET'
        })
    else:
        return jsonify({
            'status': 'Anda tidak nge-POST & nge-GET'
        })

@app.route('/predictform', methods = ['POST', 'GET'])
def predictform():
    if request.method == 'POST':
        body = request.form
        medinc = float(body['medinc'])
        houseage = float(body['houseage'])
        averooms = float(body['averooms'])
        avebedrms = float(body['avebedrms'])
        population = float(body['population'])
        aveoccup = float(body['aveoccup'])
        latitude = float(body['latitude'])
        longitude = float(body['longitude'])
        # model prediction
        hasil = model.predict([[
            medinc, houseage, averooms, avebedrms, population,
            aveoccup, latitude, longitude 
        ]])[0]
        return jsonify({
            'medinc' : body['medinc'],
            'houseage' : body['houseage'],
            'averooms' : body['averooms'],
            'avebedrms' : body['avebedrms'],
            'population' : body['population'],
            'aveoccup' : body['aveoccup'],
            'latitude' : body['latitude'],
            'longitude' : body['longitude'],
            'PRICE_PREDICTION' : hasil,
            'status': 'sukses POST'
        })
        # return render_template('result.html', body=body)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)