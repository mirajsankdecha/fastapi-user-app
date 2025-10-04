from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from app.services import predict_iris

# Define the APIRouter instance
router = APIRouter()


# Define the input data model using Pydantic
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


def get_model_from_app(request: Request):
    # Access the model saved on app.state by the startup event
    model = getattr(request.app.state, "model", None)
    if model is None:
        raise RuntimeError("Model not loaded on app.state")
    return model


@router.post("/predict")
def predict_iris_flower(iris_input: IrisInput, model=Depends(get_model_from_app)):
    # Call the predict function from services, passing the app model
    predicted_species = predict_iris(model, iris_input)
    return {"predicted_species": predicted_species}
