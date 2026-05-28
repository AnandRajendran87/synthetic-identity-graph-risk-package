import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["shared_device_flag"] = (df["shared_device_count"] >= 3).astype(int)
    df["shared_address_flag"] = (df["shared_address_count"] >= 3).astype(int)
    df["high_application_velocity_flag"] = (df["applications_30d"] >= 4).astype(int)
    df["high_graph_risk_flag"] = (df["community_risk_score"] >= 0.7).astype(int)
    df["behavioral_anomaly_flag"] = (df["behavioral_anomaly_score"] >= 0.7).astype(int)
    return df
