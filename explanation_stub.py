def explain_identity_risk(profile: dict) -> dict:
    return {
        "explanation_type": "reason_code_and_graph_feature_attribution_stub",
        "features_reviewed": list(profile.keys()),
        "note": "Replace with SHAP, graph explanation, or institution-approved explainability method."
    }
