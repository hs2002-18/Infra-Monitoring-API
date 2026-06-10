from flask import Flask
from database.db import db
from routes.health import server_bp
from routes.metric_routes import metrics_bp


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///monitor.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(server_bp)
app.register_blueprint(metrics_bp)

@app.route('/')
def home():
    return {
        "message": "Infrastructure App is up and runing"
    }

@app.route('/health')
def health():
    return{
        "status": "Healthy"
    }

@app.errorhandler(404)
def not_found(error):
    return{
        "error": "Endpoint not found"
    }, 404 

    
if __name__ == "__main__":
    app.run(debug=True)
