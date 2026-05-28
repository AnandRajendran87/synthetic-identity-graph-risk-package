from datetime import datetime, timezone
import json

def create_audit_record(identity_id: str, model_version: str, score_response: dict) -> str:
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "identity_id": identity_id,
        "model_version": model_version,
        "score_response": score_response
    }
    return json.dumps(record, indent=2)
