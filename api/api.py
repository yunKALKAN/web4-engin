"""
MUCIZEWORK WEB4 Orchestrator API
Ana giriş noktası — graph, analyze, status.
Port: 5002
"""

from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

GRAPH_PATH = os.path.join(
    os.path.dirname(__file__), "..", "storage", "graph", "graph_state.json"
)


@app.route("/")
def home():
    return jsonify({"system": "MUCIZEWORK WEB4", "status": "online"})


@app.route("/status")
def status():
    return jsonify({"status": "online", "engine": "web4_master"})


@app.route("/graph")
def graph():
    with open(GRAPH_PATH, "r", encoding="utf-8") as f:
        return jsonify(json.load(f))


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    return jsonify({
        "wallet": data.get("wallet"),
        "risk": "low",
        "cluster": "MZC",
    })


if __name__ == "__main__":
    app.run(port=5002, debug=False)
