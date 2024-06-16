import { Probot } from "probot";
import axios from "axios";

// equivalent POST request with curl:
// curl -X POST \             
//      -H "Content-Type: application/json" \
//      -d "{\"repoUrl\":\"$repoUrl\"}" \   
//         http://\[::1\]:5000/audit

export default (app: Probot) => {
  // Event handler for multiple events
  // Events: https://github.com/octokit/webhooks.js/?tab=readme-ov-file#webhook-events
  app.on(["issues", "push", "release"], async (context) => {
    const repoUrl = context.payload.repository.clone_url;

    // Send POST request to the Python API
    try {
      await axios.post("http://[::1]:5000/audit", { repoUrl });
      context.log.info(`Sent repo URL to API: ${repoUrl}`);
    } catch (error: any) {
      try {
        await axios.post("http://127.0.0.1:5000/audit", { repoUrl });
        context.log.info(`Sent repo URL to API: ${repoUrl}`);
      } catch (error: any) {
        context.log.error(`Error sending repo URL to API: ${error.message}`);
      }
    }
  });

  // Example event handler for issues opened
  app.on("issues", async (context) => {
    const issueComment = context.issue({
      body: "Thanks for opening this issue!",
    });
    await context.octokit.issues.createComment(issueComment);
  });
};
