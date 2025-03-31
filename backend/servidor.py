from flask import Flask, jsonify, request
import csv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def load_data():
    operadoras = []
    with open('operadoras.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')  
        for row in reader:
            operadoras.append(row)
    return operadoras


@app.route('/search', methods=['GET'])
def search_operadoras():
    query = request.args.get('q', '').lower()  
    data = load_data()

   
    filtered_data = [item for item in data if query in item['Nome_Fantasia'].lower()]

    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
