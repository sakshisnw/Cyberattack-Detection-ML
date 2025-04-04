import os
import pandas as pd

def load_and_merge_csv(folder_path="data"): 
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    dfs = [pd.read_csv(os.path.join(folder_path, file), low_memory=False) for file in csv_files]
    return pd.concat(dfs, ignore_index=True)

def clean_and_select_features(df):
    df[' Label'] = df[' Label'].str.strip()
    df = df.dropna(subset=['Flow Bytes/s'])
    features = ['Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
                'Fwd Packet Length Mean', 'Flow Bytes/s', 'Average Packet Size']
    X = df[features]
    y = df[' Label']
    return X, y
