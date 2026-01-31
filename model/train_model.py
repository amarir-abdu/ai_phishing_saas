import os
import sys
import pandas as pd
import joblib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.explore_data import load_csv

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(BASE_DIR, "data", "phishing_raw.csv")
MODEL_PATH = os.path.join(BASE_DIR, "saved_models", "phishing_model.pkl")


def prepare_features(df: pd.DataFrame):
    if "CLASS_LABEL" not in df.columns:
        raise KeyError("Missing reauired column: CLASS_LABEL")

    drop_cols = ["id", "CLASS_LABEL"]
    for col in drop_cols:
        if col not in df.columns:
            print(f"Warning: Column '{col}' not found, skipping drop.")

    X = df.drop(columns=[c for c in drop_cols if c in df.columns])
    y = df["CLASS_LABEL"]

    if X.empty:
        raise ValueError("Feature matrix X is empty.")

    if y.empty:
        raise ValueError("Label vector is empty.")

    print("Features and labels prepared.\n")
    print(f"Features shape: {X.shape}")
    print(f"Labels shape: {y.shape}\n")

    return X, y

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2, stratify=y)

    print("Data split into train/test.\n")
    print(f"Train size: {X_train.shape[0]}")
    print(f"Test size:  {X_test.shape[0]}\n")

    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

    model.fit(X_train, y_train)
    print("Model trained successfuly.\n")

    return model

def evaluate_model(model, X_test, y_test):
    prediction = model.predict(X_test)
    accuracy = accuracy_score(y_test, prediction)

    print("MODEL EVALUATION")
    print("-" * 40)
    print(f"Accuracy: {accuracy:.4f}\n")

    return accuracy

def save_model(model, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)

    print(f"Model saved to: {path}\n")

def main():
    df = load_csv(DATA_PATH)

    try:
        X, y = prepare_features(df)
        X_train, X_test, y_train, y_test = split_data(X, y)

        model = train_model(X_train, y_train)
        evaluate_model(model, X_test, y_test)

        save_model(model, MODEL_PATH)

    except KeyError as e:
        print(f"Column error: {e}")
    
    except ValueError as e:
        print(f"Data error: {e}")
    
    except Exception as e:
        print(f"Unexpected runtime error: {e}")


if __name__ == "__main__":
    main()