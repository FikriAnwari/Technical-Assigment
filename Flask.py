from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    if request.is_json:
        data = request.get_json()
        jarak = data.get('jarak')
        if jarak is not None:
            print(f"Received jarak: {jarak}")
            response = {
                "status": "success",
                "message": "Data received",
                "data": data
            }
            return jsonify(response), 200
        else:
            response = {
                "status": "error",
                "message": "Invalid data"
            }
            return jsonify(response), 400
    else:
        response = {
            "status": "error",
            "message": "Request must be JSON"
        }
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
