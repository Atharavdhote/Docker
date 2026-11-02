import joblib
from pathlib import Path
from fastapi import FASTAPI
from pydantic import BaseModel, Filed
BASE_DIR = Path(__file__).parent
MODEL_PATH=BASE_DIR / "model.joblib"

model = joblib.load(MODEL_PATH)

# Create a Fastapi application
app = FASTAPI(
    title = "Student Perfromance Prediction API",
    description = "Predict an expected score from study hours",
    version="1.0.0"
)
class StudentInput(BaseModel):
    study_hours: float = Filed(ge = 0,le = 0)

@app.get("/")
def home():
    return{
        "message":"Student Performance API is running"
    }
@app.get("/health")
def health():
    return{"Status":"healthy"}

@app.post("/predict")
def predict(data:StudentInput):
    prediction = model.predict([[data.study_hours]])[0]

    prediction = max(0.0, min(100.0,float(prediction)))

    return{
        "study_hours":data.study_hours,
        "predicated_score":round(prediction,2)
    }
