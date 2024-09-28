from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database to store tickets and questions
tickets = []
questions = []

@app.route('/getticket', methods=['POST'])
def get_ticket():
    # Here you might process data for ticket creation
    data = request.get_json()
    ticket_id = len(tickets) + 1  # Simple increment for demo purposes
    ticket = {
        'id': ticket_id,
        'info': data.get('info', 'No info provided')
    }
    tickets.append(ticket)
    return jsonify(ticket), 201  # Return the created ticket with 201 status

@app.route('/askquestion', methods=['POST'])
def ask_question():
    # Here you might process data for asking questions
    data = request.get_json()
    question_id = len(questions) + 1  # Simple increment for demo purposes
    question = {
        'id': ticket_id,
        'content': data.get('content', 'No content provided')
    }
    questions.append(question)
    return jsonify(question), 201  # Return the created question with 201 status

if __name__ == '__main__':
    app.run(debug=True)

