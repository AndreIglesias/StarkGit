# StarkGit

AI Certified Audit on the Starknet Blockchain

https://github.com/AndreIglesias/StarkGit/assets/107457733/71766bed-9c29-4335-8222-d98fcff67f34

## How to run the app

### Github probot app

To run the server app that connects the repository with the AI server.

```bash
npm run build && npm start
```

### Python API Server (auditor)

To run the Audit with AI server and upload the audit certification to the blockchain.

```bash
poetry run python3 -m audit
```

To test the analyzer, we can make a POST request to the API server.
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"repoUrl\": \"https://github.com/andreiglesias/starkgit.git\"}" localhost:5000/audit | jq
```
To achieve a certification like this:
```json
{
  "auditCertification": {
    "commit": "68951b9a06dea0c3215bc896118202b6763e72cb",
    "securityAnalysis": {
      "reports": {
        "audit/__init__.py": "Based on the provided code snippet, no sensitive data is directly exposed. However, I would recommend using environment variables from a secret management system instead of loading.env file directly. This mitigates the risk of exposing credentials if the file is accidentally committed to version control or falls into the wrong hands. Therefore, the report would read: 'Environment variables from a secret management system should be used instead of directly loading the.env file.'",
        "audit/__main__.py": "No security vulnerabilities found.",
        "audit/analysis.py": "No security vulnerabilities found.",
        "audit/repo.py": "Multiple potential security vulnerabilities were found in the code:\n\n1. The 'git' library is used without proper authentication checks. This could potentially lead to man-in-the-middle attacks, cloning of malicious repositories, or unauthorized access to GitHub repositories.\n2. The 'open' function is used without any error handling or validation on the file_path. This could potentially lead to reading unintended files or attempting to read malicious files.\n3. The code uses string formatting. Without proper validation, this could potentially lead to format string vulnerabilities.\n\nIt",
        "starkgit/src/index.ts": "No security vulnerabilities found.",
        "starkgit/test/index.test.ts": "No security vulnerabilities found.",
        "starkgit/vitest.config.ts": "No security vulnerabilities found."
      },
      "score": 0.7142857142857143,
      "totalFiles": 7,
      "vulnerabilitiesFound": 2
    }
  },
  "auditDate": "2024-06-23T17:56:46Z",
  "auditor": "StarkGit v1.0.0"
}
```

### Project Details

#### General Idea (2-3 sentences)
We are developing a tool that uses AI to analyze and certify the quality and security of code hosted on GitHub, generating a digital certificate that is then registered on the blockchain using Cairo and the Starknet blockchain. This ensures that code quality and security assessments are transparent, immutable, and easily verifiable by anyone.

#### What Problem Does It Solve
This project addresses the lack of transparent and reliable methods for verifying the quality and security of code in software development. By leveraging AI for comprehensive analysis and blockchain for certification, it provides a trustworthy and tamper-proof solution for developers and organizations to demonstrate the integrity and security of their code.

#### List of First 5 Users and How Do We Get Them
1. **Open Source Project Maintainers**: Reach out through GitHub repositories and open source communities, offering free trials and emphasizing the security certification aspect.
2. **Software Development Firms**: Engage through LinkedIn and professional networks, emphasizing benefits for client trust, internal quality assurance, and security.
3. **Freelance Developers**: Target via freelancing platforms and forums, highlighting the tool as a way to enhance their portfolio with verified security assessments.
4. **Educational Institutions**: Collaborate with universities and coding bootcamps to integrate the tool into their curriculum for teaching best practices in both quality and security.
5. **Security Auditors**: Connect through cybersecurity conferences and groups, presenting the tool as a supplementary audit resource with blockchain verification.

#### Demo Story
Alice, a project maintainer, releases a new version of her project on GitHub. Upon the release, a GitHub App triggers our AI tool to analyze the code for quality and security. The analysis results in a high-quality score and identifies no major security vulnerabilities, generating a digital certificate. This certificate is then automatically registered on the Starknet blockchain. Alice receives a notification with a link to the immutable certificate, which she shares with her contributors and users, proving the code's quality and security. This not only boosts confidence in her project but also attracts new contributors and users.

### Project Plan for MVP/Prototype (3 Cycles: 14 days-plan)

**Milestones and Tasks for MVP**

#### Cycle 1: Define Certification Criteria and Develop AI Analysis Tool

1. **Define Certification Criteria (1 days)**
   - Select key metrics for quality and security (e.g., code cleanliness, common security vulnerabilities).
   - Establish simple thresholds for these metrics.

2. **Develop AI Analysis Tool (3 days)**
   - Select a pre-trained AI model from Hugging Face (e.g., `CodeBERT`).
   - Implement code analysis functionality to check for cleanliness and a few common security issues.
   - Test the model with sample code snippets.

#### Cycle 2: Create Certificate Generation Process && Blockchain Integration

3. **Create Certificate Generation Process (2 days)**
   - Design a simple digital certificate format (JSON).
   - Implement code to generate a certificate with analysis results and a hash.

5. **Blockchain Integration with Cairo & Starknet (3 days)**
   - Develop a Cairo smart contract for certificate registration.
   - Set up the Starknet environment and deploy the contract.
   - Create a simple Python script to interact with the smart contract and register certificates.

#### Cycle 3: GitHub App Setup

6. **GitHub App Setup (3 days)**
   - Develop a GitHub App to automate code analysis and certificate registration upon new releases or updates to the master branch.
   - Test the app with a sample GitHub repository.

7. **Testing and Final Adjustments (2 days)**
   - Conduct end-to-end testing of the entire workflow.
   - Make necessary adjustments based on test results.

### Adjusted Goals for the MVP
- **Focus on Basic Functionality**: Prioritize simple, core features for code analysis and blockchain registration.
- **Leverage Existing Tools**: Use pre-built models and tools to minimize development time.
- **Streamline the Workflow**: Ensure the workflow is straightforward and easy to demonstrate.
