# model/train_model.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load preprocessed features
features = pd.read_csv(r"C:\Users\roshn\OneDrive\Desktop\UNSW\Term 3-2024\6841\project\data/processed_features.csv")
model_features = features.drop(columns=['user_id', 'hour'])

# Train the model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(model_features)

# Save the model
joblib.dump(model, r"C:\Users\roshn\OneDrive\Desktop\UNSW\Term 3-2024\6841\project\model/isolation_forest_model.pkl")
