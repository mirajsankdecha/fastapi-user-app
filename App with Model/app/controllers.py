# Import APIRouter to create a modular set of routes (like a mini-app)
from fastapi import APIRouter

# Import the Pydantic schema for input validation
# IrisInput defines the structure of input data (e.g., sepal/petal lengths and widths)
from app.schema import IrisInput

# Import the service function that actually makes the ML prediction
from app.services import predict_iris

# Create a router instance
# This allows you to define routes separately from the main app
router = APIRouter()

# Define a POST endpoint at "/predict"
# This means clients will send data to this URL to get a prediction
@router.post("/predict")
def predict_iris_flower(iris_input: IrisInput):
    # FastAPI automatically converts and validates the incoming JSON into an IrisInput object
    # Call the service function, passing in the validated input
    predicted_species = predict_iris(iris_input)
    
    # Return the prediction as a JSON response
    return {"predicted_species": predicted_species}
