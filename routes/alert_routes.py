from flask import Blueprint, jsonify
from services.alerts import get_alerts

alerts_bp = Blueprint(
    "alert_bp",
    __name__
)

@alerts_bp.route("/alerts", methods=["GET"])
def alerts():
    return jsonify(
        get_alerts()
    )   