import os
import time


try:
    import requests
except:
    stream = os.popen('pip install requests')
    time.sleep(40)
finally:
    import requests
try:
    import git
except:
    stream = os.popen('pip install GitPython')
    time.sleep(40)
finally:
    import git



def test():
    print("changed a super upadte")
    print("this Abba Tanim")
    repo = git.Repo(os.getcwd())
    current = repo.head.commit
    repo.remotes.origin.pull()
    if current != repo.head.commit:
                print("Git changed")