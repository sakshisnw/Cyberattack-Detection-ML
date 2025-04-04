from scripts.preprocess import load_and_merge_csv, clean_and_select_features

# Set path to your data folder (make sure it contains at least one .csv file)
folder_path = "data"

# Step 1: Load and merge CSV files
df = load_and_merge_csv(folder_path)

# Print some info to verify
print("CSV files loaded and merged.")
print(f"Shape of merged dataframe: {df.shape}")
print("Columns:", df.columns.tolist()[:5], "...")  # preview first few columns

# Step 2: Clean and select features
X, y = clean_and_select_features(df)

print("\n Features and labels extracted.")
print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
print(f"First few labels:\n{y.value_counts()}")
