# predict_image.py
import numpy as np
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from keras.utils import load_img, img_to_array
from PIL import Image

# Load model once
model = MobileNetV2(weights="imagenet")

def predict_food(img: Image.Image):
    img = img.resize((224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    label = decode_predictions(preds, top=1)[0][0][1]  # Get top prediction
    return label.replace("_", " ").title()
