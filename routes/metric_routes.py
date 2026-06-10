from flask import Blueprint, jsonify
from services.metrics import get_system_metrics

metrics_bp = Blueprint(
    "metrics_bp",
    __name__
)

@metrics_bp.route("/metrics", methods=["GET"])
def get_metrics():
    return jsonify(
        get_system_metrics()
    )