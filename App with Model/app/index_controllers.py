# Import APIRouter to create a modular set of routes
from fastapi import APIRouter

# Create a router instance for index-related endpoints
index_router = APIRouter()

# Define a POST endpoint at "/index"
# Clients can send a string value to this endpoint
@index_router.post("/index")
def index_data(index_data_name: str):
    # Simply return the received string as JSON
    # Key is "Index name", value is what client sent
    return {"Index name": index_data_name}

# Define another POST endpoint at "/update"
# Clients can send a string value to update some index
@index_router.post("/update")
def data(updated_index: str):
    # Return the received string as JSON
    # Key is "Updated index", value is what client sent
    return {"Updated index": updated_index}
