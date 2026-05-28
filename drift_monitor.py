from dataclasses import dataclass

@dataclass
class MonitoringMetrics:
    feature_drift_score: float
    alert_volume_change: float
    false_positive_rate: float
    fraud_capture_rate: float

def monitoring_status(metrics: MonitoringMetrics) -> str:
    if metrics.feature_drift_score > 0.25:
        return "FEATURE_DRIFT_REVIEW_REQUIRED"
    if metrics.alert_volume_change > 0.40:
        return "ALERT_VOLUME_REVIEW_REQUIRED"
    if metrics.false_positive_rate > 0.30:
        return "FALSE_POSITIVE_REVIEW_REQUIRED"
    return "STABLE"
