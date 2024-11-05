
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load the model
model = joblib.load(r"C:\Users\roshn\OneDrive\Desktop\UNSW\Term 3-2024\6841\project\model/isolation_forest_model.pkl")

def detect_anomalies(log_entry):
    user_features = log_entry.groupby(['user_id', 'hour', 'action_type']).size().unstack(fill_value=0).reset_index()
    anomaly_score = model.decision_function(user_features)
    return anomaly_score < -0.2  # Custom threshold
 
