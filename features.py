# scripts/feature_engineering.py
import pandas as pd

def preprocess_logs(file_path):
    logs_df = pd.read_csv(file_path)
    logs_df['timestamp'] = pd.to_datetime(logs_df['timestamp'])
    logs_df['hour'] = logs_df['timestamp'].dt.hour
    
    # Aggregate features by user and hour
    features = logs_df.groupby(['user_id', 'hour', 'action_type']).size().unstack(fill_value=0).reset_index()
    return features

# Test feature preprocessing
features = preprocess_logs(r"C:\Users\roshn\OneDrive\Desktop\UNSW\Term 3-2024\6841\project\data/synthetic_logs.csv")
features.to_csv(r"C:\Users\roshn\OneDrive\Desktop\UNSW\Term 3-2024\6841\project\data/processed_features.csv", index=False)
