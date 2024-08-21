from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Load the model
model = load_model('fashion_rating_model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Process the image
    image = Image.open(file).convert('L')  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to 28x28
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image.astype('float32') / 255.0

    # Get prediction
    predictions = model.predict(image)
    rating = np.argmax(predictions)  # Get the class with highest probability

    return jsonify({'rating': int(rating)})  # Send the rating back as JSON

if __name__ == '__main__':
    app.run(debug=True)
