from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for the entire application

@app.route('/process_image', methods=['POST'])
def process_image():
    image_data = request.form['image_data']
    return jsonify(image_data)


if __name__ == '__main__':
    app.run()  # Starts the Flask development server on http://127.0.0.1:5000/
