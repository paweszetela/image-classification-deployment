from flask import Flask, jsonify, request, render_template
from inference import get_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        img_bytes = file.read()
        class_id, class_name = get_prediction(img_bytes)
        return jsonify({'class_id': class_id, 'class_name': class_name})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
