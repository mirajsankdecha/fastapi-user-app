# Import pickle to load saved ML model and label encoder
import pickle

# Import numpy for handling numerical arrays
import numpy as np

# Load the trained ML model from a file
with open(r'C:/Users/Lenovo/Downloads/ml_project/model/best_iris_model.pkl', 'rb') as f:
    model = pickle.load(f)  # This is your trained classifier (e.g., RandomForest)

# Load the label encoder from a file
# This converts numeric predictions back to actual species names
with open(r'C:/Users/Lenovo/Downloads/ml_project/model/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Function to make predictions on new Iris data
def predict_iris(data):
    # Convert the input data (Pydantic model) into a 2D numpy array
    # [[sepal_length, sepal_width, petal_length, petal_width]]
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    
    # Use the loaded model to predict the class (numeric label)
    prediction = model.predict(features)
    
    # Convert the numeric label back to species name using label encoder
    predicted_species = label_encoder.inverse_transform([prediction[0]])[0]
    
    # Return the predicted species as a string
    return predicted_species
