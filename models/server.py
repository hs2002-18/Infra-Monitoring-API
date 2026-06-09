from database.db import db

class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    server_name = db.Column(db.String(100), nullable=False, unique=True)
    ip_address = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="healthy")

    def to_dict(self):
        return {
            "id": self.id,
            "server_name": self.server_name,
            "ip_address": self.ip_address,
            "status": self.status
        }  