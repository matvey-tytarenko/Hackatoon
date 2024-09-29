from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import uuid
from chatv1 import dawaj_odpowiedz

tickets = []

def generate_ticket():
    ticket = str(uuid.uuid4())
    tickets.append(ticket)
    return ticket

app = Flask(__name__)
CORS(app)

#@app.route('/get_ticket', methods=['GET'])
#def get_data():
#    ticket = generate_ticket()
#    tickets.append(ticket)
#    response_data = {
#        "message": ticket,
#        "status": "success",
#        "code": 200
#    }
#    return jsonify(response_data)

@app.route('/ask', methods=['POST'])
def post_data():
    try:
        # Try to get JSON data from request
        data = request.get_json()

        if data is None or 'message' not in data:
            # Return an error if the data is not valid
            return jsonify({
                "message": "Invalid request. 'message' field is required.",
                "status": "fail",
                "code": 400
            }), 400

        # If everything is okay, proceed
        response_data = {
            "message": dawaj_odpowiedz(data.get('message')),
            "status": "success",
            "code": 200
        }
        return jsonify(response_data), 200

    except Exception as e:
        # Return an error response in case of an exception
        return jsonify({
            "message": f"An error occurred: {str(e)}",
            "status": "error",
            "code": 500
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
