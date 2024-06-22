from flask import Flask, request, jsonify
from audit.repo import clone_repo, analyze_repo
import os
import subprocess
import ast

app = Flask(__name__)


@app.route("/audit", methods=["POST"])
def audit():
    data = request.json
    clone_path = clone_repo(data["repoUrl"])
    analyze_repo(clone_path)
    return jsonify({"message": "Audit complete"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
