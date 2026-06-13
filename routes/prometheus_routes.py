from flask import Blueprint, Response
from prometheus_client import generate_latest

prometheus_bp = Blueprint(
    "prometheus_bp",
    __name__
)

@prometheus_bp.route(
    "/prometheus",
    methods=["GET"]
)
def prometheus_metrics():

    return Response(
        generate_latest(),
        mimetype="text/plain"
    )