from flask import Flask
import os

app = Flask(__name__)

ENV = os.getenv("ENVIRONMENT", "dev")

@app.route("/")
def home():
    return f"Hello from {ENV} environment 🚀"

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
