from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({
        "operation_code": 1
    }), 200

@app.route('/bfhl', methods=['POST'])
def post_data():
    data = request.json.get('data', [])
    user_id = "john_doe_17091999"  # Replace with your dynamic logic
    email = "john@xyz.com"  # Replace with your email
    roll_number = "ABCD123"  # Replace with your roll number

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lowercase_alphabets = [item for item in alphabets if item.islower()]

    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

    return jsonify({
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
