import pandas as pd
import os

def load_and_merge_csv(folder_path):
    dfs = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def clean_and_select_features(df):
   
    df.columns = df.columns.str.strip()

    df = df.replace([float('inf'), float('-inf')], pd.NA)
    df = df.dropna()

    selected_features = [
        'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
        'Fwd Packet Length Mean', 'Average Packet Size'
    ]
    target_column = 'Label'

    X = df[selected_features]
    y = df[target_column]

    return X, y
