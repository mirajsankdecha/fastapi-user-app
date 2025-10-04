from fastapi import FastAPI
from app.controllers import router as api_router  # Import the router
import pickle
import uvicorn

app = FastAPI()

# Global variable to store the model
model = None

# Load the pre-trained model when the app starts
@app.on_event("startup")
def load_model():
    global model
    with open(r'C:\Users\Urmay Shah\PycharmProjects\ml_project\model\best_iris_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")

# Include the routes from the controller
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8001, reload=True)
