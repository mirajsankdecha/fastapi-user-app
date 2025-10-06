# Import BaseModel from Pydantic
# Pydantic helps FastAPI automatically validate and parse incoming data
from pydantic import BaseModel

# Define a Pydantic model for the Iris flower input
class IrisInput(BaseModel):
    # These are the features the ML model expects
    sepal_length: float  # Sepal length in cm
    sepal_width: float   # Sepal width in cm
    petal_length: float  # Petal length in cm
    petal_width: float   # Petal width in cm
