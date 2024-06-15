# StarkGit

AI Certified Audit on the Starknet Blockchian


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
