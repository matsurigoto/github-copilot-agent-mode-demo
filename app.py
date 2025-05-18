from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello, World!"

@app.route('/data', methods=['POST'])
def receive_data():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    data = request.get_json()
    # 可根據需求處理 data
    return "Received"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
