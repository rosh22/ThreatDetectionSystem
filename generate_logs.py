# scripts/generate_logs.py
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_logs(num_logs):
    users = ['user1', 'user2', 'user3']
    actions = ['login', 'file_access', 'data_transfer', 'logout']
    logs = []
    for _ in range(num_logs):
        log = {
            'user_id': random.choice(users),
            'timestamp': datetime.now() - timedelta(minutes=random.randint(0, 1440)),
            'action_type': random.choice(actions),
            'resource': random.choice(['server1', 'server2', 'file1', 'file2']),
            'action_details': 'details about the action'
        }
        logs.append(log)
    return pd.DataFrame(logs)

# Generate and save sample logs
logs_df = generate_logs(1000)
logs_df.to_csv(r"C:\Users\roshn\OneDrive\Desktop\UNSW\Term 3-2024\6841\project\data\synthetic_logs.csv", index=False)
