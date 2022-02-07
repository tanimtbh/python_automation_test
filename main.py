import time
import git
import os


while True:
    try:
        repo = git.Repo(os.getcwd())
        current = repo.head.commit
        repo.remotes.origin.pull()
        if current != repo.head.commit:
            print("changed found")
    except:
        print("Something wrong")
    finally:
        print("Yahoo from abba Tanim from finally a virsion changed")
    
    time.sleep(20)
    