import os, re, git
from audit.analysis import analyze_code

# REPONAME is the path where the repository will be cloned
# clone_repo is a function that clones the repository
# analyze_repo is a function that analyzes the repository: File by file, function by function
# use pandas to create json with certificate information


def supported_file(file_name: str) -> bool:
    extensions = {
        ".cairo",
        ".c",
        ".py",
        ".java",
        ".js",
        ".jsx",
        ".ts",
        ".tsx",
        ".php",
    }
    return any(file_name.endswith(ext) for ext in extensions)


# Step 1: Clone the repository
def clone_repo(repo_url: str) -> str:
    match = re.match(r"https://github.com/([^/]+)/([^/]+).git", repo_url)
    if not match:
        raise ValueError("Expected repo format: https://github.com/user/repo.git")
    user, repo = match.groups()
    clone_path = f"/tmp/{user}_{repo}/"
    if os.path.exists(clone_path):
        print(f"ℹ️  Repository already cloned at {clone_path}")
        try:
            # make a git pull if it's already cloned
            repo = git.Repo(clone_path)
            origin = repo.remotes.origin
            origin.pull()
            print("✅ Repository updated:", repo_url)
        except git.exc.GitCommandError as e:
            print(e)
        return clone_path
    print(f"Cloning repository from {repo_url}")
    try:
        git.Repo.clone_from(repo_url, clone_path)
        print("✅ Repository cloned:", repo_url)
        print("ℹ️  Clone path:", clone_path)
    except git.exc.GitCommandError as e:
        print(e)
    return clone_path


# Step 2: Analyze the repository
def analyze_repo(clone_path: str):
    print("Analyzing repository:", clone_path)
    files = {"File": [], "Content": []}
    for root, _, filenames in os.walk(clone_path):
        print(f"📁 {root}")
        for filename in filenames:
            file_path = os.path.join(root, filename)
            if not supported_file(file_path):
                continue
            print(f" 📄 {filename}")
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    print(analyze_code(content))
                    print(f"✅ Read file: {file_path}")
            except UnicodeDecodeError:
                print(f"❌ Could not read file: {file_path}")
                continue
            files["File"].append(file_path)
            files["Content"].append(content)
    print("✅ Repository analyzed")
