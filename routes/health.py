from flask import Blueprint, jsonify, request
from database.db import db
from models.server import Server

server_bp = Blueprint('server_bp', __name__)
@server_bp.route("/register-server", methods=["POST"])
def register_server():

    data = request.get_json()
    
    if not data or "server_name" not in data or "ip_address" not in data:
        return jsonify({
            "message": "Invalid request data"
        }), 400
    
    existing_server = Server.query.filter_by(
        ip_address=data["ip_address"]
    ).first()

    if existing_server:
        return jsonify({
            "error": "Server alreasy exists!"
        })

    new_server = Server(
        server_name=data["server_name"],
        ip_address=data["ip_address"]
    )

    db.session.add(new_server)
    db.session.commit()

    return jsonify({
        "message": "Server registered successfully"
    }), 201

@server_bp.route("/servers", methods=["GET"])
def get_servers():

    servers = Server.query.all()

    return jsonify([
        server.to_dict()
        for server in servers
    ])