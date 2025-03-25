from flask import Flask, request, jsonify
from mpmath import mp
import argparse

app = Flask(__name__)

def compute_pi(decimals):
    mp.dps = decimals
    return str(mp.pi)

def compute_nth_decimal(n):
    if n == 0 :
      return '3'
    mp.dps = n + 10 
    return str(mp.pi)[n + 1]

@app.route('/pi', methods=['GET'])
def get_pi():
    try:
        decimals = int(request.args.get('decimals', 1))
        if decimals < 0:
            return jsonify({"error": "decimals must be a positive integer."}), 400
        result = compute_pi(decimals)
        return jsonify({"pi": result})
    except ValueError:
        return jsonify({"error": "Invalid input for decimals."}), 400

@app.route('/pi_digit', methods=['GET'])
def get_pi_digit():
    try:
        position = int(request.args.get('position', 1))
        if position < 1:
            return jsonify({"error": "Position must be a positive integer."}), 400
        digit = compute_nth_decimal(position)
        if digit is None:
            return jsonify({"error": "Position out of range."}), 400
        return jsonify({"digit": digit})
    except ValueError:
        return jsonify({"error": "Invalid input for position."}), 400

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Pi calculation service.")
    parser.add_argument('--port', type=int, default=6000, help="Port to run the server on.")
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port)

