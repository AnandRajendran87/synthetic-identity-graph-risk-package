from fastapi import FastAPI
from pydantic import BaseModel
from src.inference.score_identity import score_identity

app = FastAPI(title="Synthetic Identity Fraud Detection API")

class IdentityProfile(BaseModel):
    shared_device_count: int
    shared_address_count: int
    shared_phone_count: int
    applications_30d: int
    account_age_days: int
    transaction_velocity_24h: int
    graph_centrality_score: float
    community_risk_score: float
    behavioral_anomaly_score: float

@app.get("/")
def health_check():
    return {"status": "ok", "service": "synthetic-identity-graph-risk"}

@app.post("/score-identity")
def score(profile: IdentityProfile):
    return score_identity(profile.model_dump())
