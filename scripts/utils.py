import joblib
import os

def save_model(model, filename, folder="models"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    joblib.dump(model, os.path.join(folder, filename))

def load_model(filename, folder="models"):
    return joblib.load(os.path.join(folder, filename))
