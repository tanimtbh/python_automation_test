import git
import os
repo = git.Repo(os.getcwd())
current = repo.head.commit
repo.remotes.origin.pull()
if current != repo.head.commit:
            print("changed found")