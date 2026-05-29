from flask import Flask
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
