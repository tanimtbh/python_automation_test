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
    print("call test() why")
    repo = git.Repo(os.getcwd())
    current = repo.head.commit
    repo.remotes.origin.pull()
    if current != repo.head.commit:
                print("Git changed")
                print("Git changed")
                print("Git changed")
                print("Git changed")
                print("Git changed")
test()