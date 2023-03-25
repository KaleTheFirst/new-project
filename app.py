import database as db
from flask import Flask, render_template, request
import requests





app = Flask(__name__)

@app.route('/')
def index():
    

    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        inputa = request.args['fname']
    else:
        inputa = request.form['fname']
    
    response = requests.get(f'http://api.aviationstack.com/v1/flights?access_key=42c1b498145ddb1f3d0c5d019f27e7b4&arr_icao={inputa}')
    data = response.json()
    print(data)

    flights = []

    for data_point in data['data']:
        flight = {
            'date': data_point['flight_date'],
            'departure_airport': data_point['departure']['airport'],
            'departure_scheduled': data_point['departure']['scheduled'],
            'arrival_airport': data_point['arrival']['airport'],
            'arrival_scheduled': data_point['arrival']['scheduled'],
            'airline': data_point['airline']['name'],
            'aircraft': data_point['aircraft']['registration']

        }   
        flights.append(flight)

    db.insert_flight(flights)
    data = db.get_all_flights()

    return render_template('arrivals.html' , data = data)


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')