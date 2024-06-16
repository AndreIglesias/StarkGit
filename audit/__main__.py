from flask import Flask, request, jsonify
import os
import subprocess
import ast

app = Flask(__name__)


def clone_repo(repo_url):
    print("REPO:", repo_url)


@app.route("/audit", methods=["POST"])
def audit():
    data = request.json
    clone_repo(data["repoUrl"])
    return jsonify({"message": "Audit complete"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)