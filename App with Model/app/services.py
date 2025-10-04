import pickle
import numpy as np
from pathlib import Path


# Attempt to load the label encoder from the project's model directory
base_dir = Path(__file__).resolve().parents[1]
label_encoder_path = base_dir / "model" / "label_encoder.pkl"
if not label_encoder_path.exists():
    raise FileNotFoundError(f"Label encoder not found at {label_encoder_path}")

with label_encoder_path.open("rb") as f:
    label_encoder = pickle.load(f)


# Function to make predictions
def predict_iris(model, data):
    # Get the feature values from the request
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])

    # Predict the species using the loaded model (model returns a numeric label)
    prediction = model.predict(features)

    # Convert the numeric label back to the species name using the label encoder
    predicted_species = label_encoder.inverse_transform([prediction[0]])[0]

    return predicted_species  # Return the predicted species name
