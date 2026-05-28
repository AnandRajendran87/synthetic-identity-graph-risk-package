from src.inference.score_identity import reason_codes

def test_shared_device_reason_code():
    reasons = reason_codes({
        "shared_device_count": 4,
        "shared_address_count": 1,
        "shared_phone_count": 1,
        "applications_30d": 1,
        "community_risk_score": 0.2,
        "behavioral_anomaly_score": 0.1
    })
    assert "Device shared across multiple identities" in reasons
