from flask import Flask, request, jsonify
from audit.repo import clone_repo, analyze_repo
from datetime import datetime, timezone
import audit as aud

app = Flask(__name__)


@app.route("/audit", methods=["POST"])
def audit():
    REPORTS = {}
    VULNERABILITIES = {"found": 0, "not_found": 0}
    data = request.json
    clone_path, commit_sha = clone_repo(data["repoUrl"])
    print("Commit SHA", commit_sha)
    REPORTS, VULNERABILITIES = analyze_repo(clone_path, REPORTS, VULNERABILITIES)
    if VULNERABILITIES["found"] + VULNERABILITIES["not_found"] == 0:
        return jsonify(
            {
                "error": "No supported files found in the repository. Supported files are: .cairo, .c, .py, .java, .js, .jsx, .ts, .tsx, .php"
            },
            400,
        )
    score = VULNERABILITIES["not_found"] / (
        VULNERABILITIES["found"] + VULNERABILITIES["not_found"]
    )
    audit_json = {
        "auditCertification": {
            "commit": commit_sha,
            "securityAnalysis": {
                "score": score,
                "vulnerabilitiesFound": VULNERABILITIES["found"],
                "totalFiles": VULNERABILITIES["found"] + VULNERABILITIES["not_found"],
                "reports": REPORTS,
            },
        },
        "auditDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "auditor": f"{aud.__package_name__} v{aud.__version__}",
    }
    return jsonify(audit_json), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
