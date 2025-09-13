from fastapi import FastAPI
import uvicorn
from logic import create_info   # 👈 import function from logic.py

app = FastAPI()

@app.get("/")  # simple route
def read_root():
    return {"Hello": "World"}

@app.get("/getinfo")
def getinfom(name: str):
    return {"message": f"welcome to the world : {name}"}

@app.post("/createuser")
def create_user_route(name: str, phone: str, age: int):
    ans = create_info(name, phone, age)   # 👈 use helper function
    if ans:
        return {
            "status": "user created successfully",
            "name": name,
            "phone": phone,
            "age": age
        }
    else:
        return {"status": "user creation failed"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)
