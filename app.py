from flask import Flask, jsonify
import time
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home page accessed")
    return "<h1>Cloud App Deployed on Render</h1><p>Status: Running</p>"

@app.route("/health")
def health():
    return jsonify(status="UP", service="render-cloud-app"), 200

@app.route("/load")
def simulate_load():
    app.logger.warning("Simulating CPU load for monitoring test...")
    # Brief CPU-intensive task
    total = sum(i * i for i in range(5_000_000))
    return jsonify(message="Load test complete", result=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)