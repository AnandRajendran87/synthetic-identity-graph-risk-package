import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from src.features.build_features import build_features

DATA_PATH = "data/sample/sample_synthetic_identity_profiles.csv"
MODEL_PATH = "src/models/synthetic_identity_model.joblib"

FEATURES = [
    "shared_device_count", "shared_address_count", "shared_phone_count",
    "applications_30d", "account_age_days", "transaction_velocity_24h",
    "graph_centrality_score", "community_risk_score", "behavioral_anomaly_score",
    "shared_device_flag", "shared_address_flag", "high_application_velocity_flag",
    "high_graph_risk_flag", "behavioral_anomaly_flag"
]

def train():
    df = build_features(pd.read_csv(DATA_PATH))
    X = df[FEATURES]
    y = df["synthetic_fraud_label"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42
    )
    model = RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)
    print(classification_report(y_test, model.predict(X_test), zero_division=0))
    joblib.dump(model, MODEL_PATH)

if __name__ == "__main__":
    train()
