# Importing necessary libraries
import Encode  # (Looks unused — you can remove this import if not needed)
import pandas as pd
from sklearn.model_selection import train_test_split  # To split data into training & testing
from sklearn.metrics import f1_score                  # To evaluate model performance
from sklearn.ensemble import RandomForestClassifier   # Machine learning model
from sklearn.svm import SVC                           # Support Vector Classifier model
from sklearn.tree import DecisionTreeClassifier        # Decision Tree model
from sklearn.naive_bayes import GaussianNB             # Naive Bayes model
from sklearn.preprocessing import LabelEncoder         # To convert text labels into numbers
import pickle                                          # To save models into files

# ---------------------------------------------------------------------
# Function: train_model
# Purpose: Train multiple models on the Iris dataset, compare them, 
#          and save the best one for later use.
# ---------------------------------------------------------------------
def train_model(file_path):
    # 1️⃣ Load the Iris dataset from CSV
    df = pd.read_csv(file_path)

    # 2️⃣ Define input features (X) and target/output (y)
    # X -> all the numeric measurements
    # y -> species (the flower name)
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['species']

    # 3️⃣ Encode the species names (text) into numeric labels
    # Example: setosa -> 0, versicolor -> 1, virginica -> 2
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # 4️⃣ Print the label mapping (for reference)
    label_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
    print(f"Label mapping: {label_mapping}")

    # 5️⃣ Split dataset into training and testing parts
    # 70% of data for training, 30% for testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.3, random_state=42
    )

    # 6️⃣ Initialize multiple ML models for comparison
    models = {
        'RandomForest': RandomForestClassifier(),
        'SVC': SVC(),
        'DecisionTree': DecisionTreeClassifier(),
        'NaiveBayes': GaussianNB()
    }

    # 7️⃣ Train each model, test it, and measure F1 score
    best_model = None
    best_f1 = 0  # To store the best F1 score
    for name, model in models.items():
        model.fit(X_train, y_train)  # Train the model
        y_pred = model.predict(X_test)  # Test the model on test data
        f1 = f1_score(y_test, y_pred, average='weighted')  # Measure performance
        print(f'{name}: F1 Score = {f1}')

        # 8️⃣ Keep track of the best model
        if f1 > best_f1:
            best_f1 = f1
            best_model = model

    # 9️⃣ Save (pickle) the best model and the label encoder for later use
    with open('model/best_iris_model.pkl', 'wb') as f:
        pickle.dump(best_model, f)  # Saves trained model to file

    with open('model/label_encoder.pkl', 'wb') as f:
        pickle.dump(label_encoder, f)  # Saves label encoder to file

    # 🔟 Print summary of which model performed the best
    print(f'Best model is {best_model} with F1 score: {best_f1}')


# ---------------------------------------------------------------------
# Run this script directly (not when imported)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Path to your dataset file
    file_path = r"C:/Users/Lenovo/Downloads/ml_project/data/Iris.csv"

    # Call the training function
    train_model(file_path)
