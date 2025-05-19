from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import json
import numpy as np

app = FastAPI(title="ML Model Deployment API")

models = {
    "random_forest": joblib.load("models/random_forest_model.pkl"),
    "ridge": joblib.load("models/ridge_model.pkl"),
    "decision_tree": joblib.load("models/decision_tree_model.pkl"),
    "linear": joblib.load("models/linear_model.pkl")
}

with open("models/model_performance.json") as f:
    model_performance = json.load(f)

class InputData(BaseModel):
    model_name: str
    TOTAL_COAL_FLOW: float
    GEN_ACTIVE_POWER: float
    ECON_OUT_WTR_TEMP_R: float

@app.get("/")
def root():
    return {"message": "ML Model Deployment API is running."}

@app.post("/predict")
def predict(data: InputData):
    model_name = data.model_name
    if model_name not in models:
        raise HTTPException(status_code=404, detail="Model not found")
    
    model = models[model_name]

    input_dict = data.dict()
    input_dict.pop("model_name")
    df = pd.DataFrame([input_dict])

    prediction = model.predict(df)
    
    return {"model": model_name, "prediction": prediction.tolist()}

@app.get("/model-performance")
def get_model_performance():
    return model_performance

@app.get("/best-model")
def get_best_model():
    best_model = max(model_performance, key=lambda k: model_performance[k]["score"])
    return {
        "best_model": best_model,
        "score": model_performance[best_model]["score"]
    }
