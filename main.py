from fastapi import FastAPI
import uvicorn
import json
from logic import create_info, create_user, create_new_user_table

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Create new table at app start
    create_new_user_table()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# ✅ Old Method (uses old table: user_info)
@app.post("/createuser")
def create_user_route(name: str, age: int):
    ans = create_info(name, age)
    if ans:
        return {"status": "User created successfully (old table)", "name": name, "age": age}
    else:
        return {"status": "User creation failed (old table)"}

# ✅ New Method (uses new table: new_user_info)
@app.post("/createuserjson")
def create_user_json_route(user_json: dict):
    print("Received JSON:", user_json)
    keys = user_json.keys()
    valid_keys = ["first_name", "age", "gender", "country"]
    flag = set(keys) & set(valid_keys)
    print("Keys present:", flag)
    # ans = create_user(json.dumps(user_json)) # Convert dict to JSON string for processing in logic.py # lOAD JSON
    # if ans:
    #     return {"status": "User created successfully (new table)", "user": user_json}
    # else:
    #     return {"status": "User creation failed (new table)"}
