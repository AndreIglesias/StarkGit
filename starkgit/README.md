# StarkGit

> A GitHub App built with [Probot](https://github.com/probot/probot) that AI Certified Audit

## Setup

```sh
# Install dependencies
npm install

# Run the bot
npm start
```

## Docker

```sh
# 1. Build container
docker build -t StarkGit .

# 2. Start container
docker run -e APP_ID=<app-id> -e PRIVATE_KEY=<pem-value> StarkGit
```

## Contributing

If you have suggestions for how StarkGit could be improved, or want to report a bug, open an issue! We'd love all and any contributions.

For more, check out the [Contributing Guide](CONTRIBUTING.md).

## License

[ISC](LICENSE) © 2024 AndreIglesias & 3lsy
curl -X POST -H "Content-Type: application/json" -d "{\"repoUrl\": \"https://github.com/3lsy/auditcert\"}" localhost:5000/audit
