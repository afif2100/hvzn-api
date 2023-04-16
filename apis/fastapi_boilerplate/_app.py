from fastapi import FastAPI, Request, Body
import joblib
import numpy as np
import json
from pydantic import BaseModel


class Item(BaseModel):
    age: int
    bmi: float


app = FastAPI()


class PredictionModel():

    def __init__(self) -> None:
        self.model = joblib.load('model/model.pkl')

    def predict(self, age, bmi):
        result = self.model.predict([[age, bmi]])

        if result[0] == 1:
            result = 'Diabetes'
        else:
            result = 'Not Diabetes'

        return result


predict_function = PredictionModel()


@app.get("/")
async def read_main():
    return {"message":"Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/predict")
async def predict(payload: dict = Body(...)):

    # Get body content
    data = payload['data']
    data = np.array([data])

    # Load the model
    model = joblib.load('model/model.pkl')

    # Make the prediction
    prediction = model.predict(data)

    if prediction[0] == 1:
        result = 'Diabetes'
    else:
        result = 'Not Diabetes'

    # Return the prediction
    return {"prediction": result}

@app.post("/predict2")
async def predict2(item: Item ):
    return {"age": item.age, "bmi": item.bmi}

@app.post("/predict3")
async def predict3(item: Item ):
    return predict_function.predict(item.age, item.bmi)
