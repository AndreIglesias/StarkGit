# from audit import (
# )
import os, re, git

# REPONAME is the path where the repository will be cloned
# clone_repo is a function that clones the repository
# analyze_repo is a function that analyzes the repository: File by file, function by function
# use pandas to create json with certificate information

# Step 1: Clone the repository
def clone_repo(repo_url: str) -> str:
	match = re.match(r"https://github.com/([^/]+)/([^/]+).git", repo_url)
	if not match:
		raise ValueError("Expected repo format: https://github.com/user/repo.git")
	user, repo = match.groups()
	clone_path = f"/tmp/{user}_{repo}/"
	if os.path.exists(clone_path):
		try:
			# make a git pull if it's already cloned
			repo = git.Repo(clone_path)
			origin = repo.remotes.origin
			origin.pull()
			# git.Repo(clone_path).remotes.origin.pull()
			print("Repository updated:", repo_url)
		except git.exc.GitCommandError as e:
			print(e)
		return clone_path
	print(f"Cloning repository from {repo_url}")
	try:
		git.Repo.clone_from(repo_url, clone_path)
		print("Repository cloned:", repo_url)
		print("Clone path:", clone_path)
	except git.exc.GitCommandError as e:
		print(e)
	return clone_path

# Step 2: Analyze the repository
def analyze_repo(clone_path: str):
	print("Analyzing repository:", clone_path)