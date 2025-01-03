from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import uvicorn

app = FastAPI()
# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)
# Define the data model
class FuelData(BaseModel):
    petrolstock: float
    petroldensity: float
    petrolrate: float
    dieselstock: float
    dieseldensity: float
    dieselrate: float

# File to store JSON data
DATA_FILE = "fuel_data.json"

# Load data from the JSON file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Default data if file does not exist
        return {
            "petrolstock": 50,
            "petroldensity": 0.8,
            "petrolrate": 102.5,
            "dieselstock": 100,
            "dieseldensity": 0.85,
            "dieselrate": 90.5,
        }
# Get fuel data
@app.get("/fuel-data", response_model=FuelData)
async def get_fuel_data():
    fuel_data = load_data()
    return fuel_data

# Save data to the JSON file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
@app.put("/update-fuel-data", response_model=FuelData)
async def update_fuel_data(new_data: FuelData):
    data = new_data.dict()
    save_data(data)  # Save the updated data to the JSON file
    return data
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
