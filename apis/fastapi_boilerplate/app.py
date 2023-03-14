from fastapi import FastAPI, Request, Body
import joblib
import numpy as np
import json

app = FastAPI()


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
    print(data)


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