import git
import os
def test():
    print("changed a super upadte")
    print("this Abba Tanim")
    repo = git.Repo(os.getcwd())
    current = repo.head.commit
    repo.remotes.origin.pull()
    if current != repo.head.commit:
                print("changed found from other side")