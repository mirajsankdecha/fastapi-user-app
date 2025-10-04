import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import pickle

def train_model(file_path):
    # Load Iris dataset
    df = pd.read_csv(file_path)

    # Define features and target
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['species']

    # Encode species names to numeric labels (setosa: 0, versicolor: 1, virginica: 2)
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Print the mapping between labels and species
    label_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
    print(f"Label mapping: {label_mapping}")

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

    # Initialize models to compare
    models = {
        'RandomForest': RandomForestClassifier(),
        'SVC': SVC(),
        'DecisionTree': DecisionTreeClassifier(),
        'NaiveBayes': GaussianNB()
    }

    # Train each model and evaluate based on F1 score
    best_model = None
    best_f1 = 0
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        f1 = f1_score(y_test, y_pred, average='weighted')
        print(f'{name}: F1 Score = {f1}')

        # Keep track of the best model
        if f1 > best_f1:
            best_f1 = f1
            best_model = model

    # Dump the best model and label encoder to the file system
    with open('model/best_iris_model.pkl', 'wb') as f:
        pickle.dump(best_model, f)

    with open('model/label_encoder.pkl', 'wb') as f:
        pickle.dump(label_encoder, f)

    print(f'Best model is {best_model} with F1 score: {best_f1}')

if __name__ == "__main__":
    file_path=r"D:\NSB\Iris.csv"
    train_model(file_path)