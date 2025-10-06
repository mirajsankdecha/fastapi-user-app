# Import FastAPI class to create the web application
from fastapi import FastAPI

# Import routers from your application modules
# api_router is from app.controllers
# in_ro (index_router) is from app.index_controllers
from app.controllers import router as api_router
from app.index_controllers import index_router as in_ro

# Import pickle to load the pre-trained ML model
import pickle

# Import uvicorn to run the FastAPI app
import uvicorn

# Create an instance of FastAPI, this is your main web app
app = FastAPI()

# Global variable to store the loaded ML model
# This allows other parts of the app to use the model
model = None

# Define a startup event that runs when the FastAPI app starts
@app.on_event("startup")
def load_model():
    global model  # Access the global 'model' variable
    # Open the saved ML model file in binary read mode
    with open(r"C:/Users/Lenovo/Downloads/ml_project/model/best_iris_model.pkl", 'rb') as f:
        # Load the model from the file using pickle
        model = pickle.load(f)
    # Print confirmation that model is loaded
    print("Model loaded successfully!")

# Include routers from other modules to handle specific API routes
# This connects the endpoints defined in your controllers to the main app
app.include_router(api_router)
app.include_router(in_ro)

# If this file is run directly (not imported as a module), start the server
if __name__ == "__main__":
    # Run the FastAPI app using uvicorn
    # "main:app" -> main.py file, app object inside it
    # host="127.0.0.1" -> run locally
    # port=8002 -> access at localhost:8002
    # reload=True -> automatically reloads the server on code changes
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)
