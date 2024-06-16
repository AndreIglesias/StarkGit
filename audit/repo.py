from audit import (
	REPO_PATH,
)
import os, re, git

# REPONAME is the path where the repository will be cloned
# clone_repo is a function that clones the repository
# analyze_repo is a function that analyzes the repository: File by file, function by function
# use pandas to create json with certificate information

# Step 1: Clone the repository
def clone_repo(repo_url: str):
	print(f"Cloning repository from {repo_url}")
	match = re.match(r"https://github.com/([^/]+)/([^/]+)", repo_url)
	if not match:
		raise ValueError(f"Expected repo format: https://github.com/user/repo")
	user, repo = match.groups()
	global REPO_PATH
	REPO_PATH = f"/tmp/{user}_{repo}/"
	if os.path.exists(REPO_PATH):
		return REPO_PATH
    #gr.Info(f"Cloning repository from {repo_url}")
	try:
		git.Repo.clone_from(f"https://github.com/{user}/{repo}.git", REPO_PATH)
	except git.exc.GitCommandError as e:
		print(e)
    # global github_repository
    # github_repository = REPO_PATH
    # return REPO_PATH
    
# def extract_repo(repo_path: str):
# 	files = {"File": [], "Content": []}
# 	for root, _, filenames in os.walk(repo_path):
# 		for filename in filenames:
# 			file_path = os.path.join(root, filename)
# 			if is_media_file(filename) or ".git" in file_path:
# 				continue
# 			try:
# 				with open(file_path, "r", encoding="utf-8") as file:
# 					content = file.read()
# 			except UnicodeDecodeError:
# 				continue
# 			files["File"].append(os.path.relpath(file_path, repo_path))
# 			files["Content"].append(content)
# 	return files