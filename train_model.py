
import joblib
from pathlib import Path
from sklearn.linear_model import LinearRegression

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "model.joblib"

def train_model():
    study_hours = [
        [1], [2], [3], [4], [5],
        [6], [7], [8], [9], [10]
    ]

    student_scores = [
        35, 40, 50, 55, 60,
        68, 75, 80, 90, 95
    ]

    model = LinearRegression()
    model.fit(study_hours, student_scores)

    joblib.dump(model, MODEL_PATH)

    print("ML Model trained successfully!")
    print(f"Model saved at: {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
