import git
import os
print("yaya")
repo = git.Repo(os.getcwd())
current = repo.head.commit
repo.remotes.origin.pull()
if current != repo.head.commit:
            print("changed found from other side")