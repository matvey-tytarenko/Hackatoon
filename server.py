from flask import Flask, request, jsonify
import uuid
import time

app = Flask(__name__)

# A dictionary to store tickets and their expiration time
tickets = {}

# Ticket validity duration in seconds (1 minute)
TICKET_VALIDITY_DURATION = 60


# Function to generate a new ticket
def generate_ticket():
    ticket_id = str(uuid.uuid4())  # Generate unique ticket using uuid
    expiration_time = time.time() + TICKET_VALIDITY_DURATION
    tickets[ticket_id] = expiration_time
    return ticket_id


# Route to handle /getticket request
@app.route('/getticket', methods=['POST'])
def get_ticket():
    # Generate a new ticket
    ticket_id = generate_ticket()
    return jsonify({"ticket": ticket_id, "message": "Ticket generated successfully."}), 200


# Helper function to check if the ticket is valid
def is_ticket_valid(ticket_id):
    if ticket_id in tickets:
        expiration_time = tickets[ticket_id]
        current_time = time.time()
        if current_time <= expiration_time:
            return True
        else:
            del tickets[ticket_id]  # Ticket expired, so remove it
    return False


# Route to handle /ticketid/askquestion requests
@app.route('/<ticket_id>/askquestion', methods=['POST'])
def ask_question(ticket_id):
    # Validate the ticket
    if is_ticket_valid(ticket_id):
        # Get the question from the request
        data = request.get_json()
        question = data.get('question', None)

        if not question:
            return jsonify({"error": "No question provided."}), 400

        # Process the question (you can modify this logic as needed)
        return jsonify({"message": "Question received successfully.", "question": question}), 200
    else:
        return jsonify({"error": "Invalid or expired ticket."}), 403


if __name__ == '__main__':
    app.run(debug=True)

