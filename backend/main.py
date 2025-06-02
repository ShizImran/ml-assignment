from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import mlflow.sklearn
import os

# ---------------------
# Load MLflow model
# ---------------------
#mlflow_model_path = r"C:\ml_app_assignment\ml\mlruns\160842011003966785\b2bebc2678ba4865975455840df6df96\artifacts\mlflow_model"

try:
    mlflow_model_path = "./mlflow_model"
    model = mlflow.sklearn.load_model(mlflow_model_path)
except Exception as e:
    raise RuntimeError(f"Failed to load model from MLflow path: {e}")

# ---------------------
# Define FastAPI app and schema
# ---------------------
app = FastAPI(
    title="Personality Prediction API",
    description="Predicts whether a person is an Introvert or Extrovert using MLflow model.",
    version="1.0"
)

class PersonalityFeatures(BaseModel):
    Time_spent_Alone: int
    Stage_fear: int  # 1 = Yes, 0 = No
    Social_event_attendance: int
    Going_outside: int
    Drained_after_socializing: int  # 1 = Yes, 0 = No
    Friends_circle_size: int
    Post_frequency: int

# ---------------------
# Root route
# ---------------------
@app.get("/")
def root():
    return {"message": "Welcome to the Personality Predictor API using MLflow!"}

# ---------------------
# Prediction route
# ---------------------
@app.post("/predict")
def predict(features: PersonalityFeatures):
    # Convert input to numpy array
    input_array = np.array([[ 
        features.Time_spent_Alone,
        features.Stage_fear,
        features.Social_event_attendance,
        features.Going_outside,
        features.Drained_after_socializing,
        features.Friends_circle_size,
        features.Post_frequency
    ]])

    # Predict
    prediction = model.predict(input_array)[0]  # numpy.int64
    
    # Convert to native int to avoid JSON serialization error
    prediction_int = int(prediction)

    label = "Extrovert" if prediction_int == 1 else "Introvert"

    return {
        "prediction": label,       # string label
        "label": prediction_int,   # int label
        "input": features.dict()
    }