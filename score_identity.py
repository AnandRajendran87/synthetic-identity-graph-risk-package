import joblib
import pandas as pd
from src.features.build_features import build_features

FEATURES = [
    "shared_device_count", "shared_address_count", "shared_phone_count",
    "applications_30d", "account_age_days", "transaction_velocity_24h",
    "graph_centrality_score", "community_risk_score", "behavioral_anomaly_score",
    "shared_device_flag", "shared_address_flag", "high_application_velocity_flag",
    "high_graph_risk_flag", "behavioral_anomaly_flag"
]

def reason_codes(profile: dict) -> list:
    reasons = []
    if profile.get("shared_device_count", 0) >= 3:
        reasons.append("Device shared across multiple identities")
    if profile.get("shared_address_count", 0) >= 3:
        reasons.append("Address shared across multiple identities")
    if profile.get("shared_phone_count", 0) >= 3:
        reasons.append("Phone shared across multiple identities")
    if profile.get("applications_30d", 0) >= 4:
        reasons.append("High application velocity")
    if profile.get("community_risk_score", 0) >= 0.7:
        reasons.append("High-risk graph community")
    if profile.get("behavioral_anomaly_score", 0) >= 0.7:
        reasons.append("Behavioral anomaly detected")
    return reasons

def score_identity(profile: dict, model_path: str = "src/models/synthetic_identity_model.joblib") -> dict:
    model = joblib.load(model_path)
    df = build_features(pd.DataFrame([profile]))
    probability = float(model.predict_proba(df[FEATURES])[0][1])
    if probability >= 0.80:
        decision = "BLOCK_OR_ESCALATE"
    elif probability >= 0.50:
        decision = "STEP_UP_VERIFICATION"
    else:
        decision = "APPROVE_WITH_MONITORING"
    return {
        "synthetic_identity_probability": round(probability, 4),
        "decision": decision,
        "reason_codes": reason_codes(profile)
    }
