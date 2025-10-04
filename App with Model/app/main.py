from fastapi import FastAPI
from app.controllers import router as api_router  # Import the router
import pickle
import uvicorn
import os

app = FastAPI()

# Load the pre-trained model when the app starts
@app.on_event("startup")
def load_model():
    model_path = r"C:/Users/Lenovo/Downloads/ml_project/model/best_iris_model.pkl"
    with open(model_path, "rb") as f:
        app.state.model = pickle.load(f)   # ✅ store in app.state
    print("Model loaded successfully!")

# Include the routes from the controller
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8001, reload=True)
