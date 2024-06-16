from audit import (
	REPO_PATH,
)
import os, re, git

# REPONAME is the path where the repository will be cloned
# clone_repo is a function that clones the repository
# analyze_repo is a function that analyzes the repository: File by file, function by function
# use pandas to create json with certificate information