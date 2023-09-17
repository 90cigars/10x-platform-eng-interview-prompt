import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

# Read the CSV file and convert it to a list of dictionaries
def csv_to_json(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Load the CSV data
csv_file = 'seattle-weather.csv'
json_data = csv_to_json(csv_file)

# Route to get all weather data in JSON format
@app.route('/', methods=['GET'])
def get_weather_data():
    return jsonify(json_data)

# Route to query data with options for limit, date, and weather
@app.route('/query', methods=['GET'])
def multi_query():
    limit = int(request.args.get('limit', -1))
    date = request.args.get('date')
    weather = request.args.get('weather')

    filtered_data = json_data

    if date:
        filtered_data = [entry for entry in filtered_data if entry['date'] == date]

    if weather:
        filtered_data = [entry for entry in filtered_data if entry['weather'] == weather]

    if limit > 0:
        filtered_data = filtered_data[:limit]

    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
