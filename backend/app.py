from flask import Flask, jsonify
from flask_cors import CORS
from etl_logic import run_pipeline
from data_gen import generate_csv  

app = Flask(__name__)
CORS(app)

# Route 1: Generate the Data
@app.route('/generate-data', methods=['POST'])
def trigger_generation():
    result = generate_csv()
    return jsonify(result)

# Route 2: Process the Data (ETL)
@app.route('/trigger-etl', methods=['POST'])
def trigger_etl():
    result = run_pipeline()
    if "error" in result:
        return jsonify(result), 400
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5001, debug=True)