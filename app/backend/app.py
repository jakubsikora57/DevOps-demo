from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)


@app.route("/")
def home():
    return jsonify({
        "name": "DevOps-demo",
        "message": "Simple DevOps demo"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/tasks")
def tasks():
    return jsonify([
        {"id": 1, "title": "Learn Docker"},
        {"id": 2, "title": "Learn Kubernetes"},
        {"id": 3, "title": "Learn Terraform"}
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
