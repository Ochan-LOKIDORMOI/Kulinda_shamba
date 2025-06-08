from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import base64
import io
import pandas as pd
import datetime
import os

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("model/")

# Constants
categories = ['Elephant', 'Monkey', 'Buffalo']
IMG_SIZE = 150

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.route('/testimonies')
def testimonies():
    return render_template('testimonies.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract image
        data = request.json['image']
        image_data = base64.b64decode(data.split(',')[1])
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
        image = image.resize((IMG_SIZE, IMG_SIZE))
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction)
        confidence = float(prediction[0][predicted_index])
        predicted_label = categories[predicted_index]

        # Timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Log to CSV
        log_entry = pd.DataFrame([[timestamp, predicted_label, round(confidence * 100, 2)]],
                                 columns=["Time", "Animal", "Confidence (%)"])
        try:
            existing = pd.read_csv("logs.csv")
            updated = pd.concat([existing, log_entry], ignore_index=True)
        except Exception:
            updated = log_entry
        updated.to_csv("logs.csv", index=False)

        return jsonify({
            "label": predicted_label,
            "confidence": f"{confidence:.2%}",
            "time": timestamp
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
