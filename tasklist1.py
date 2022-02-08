#deafult python library import
import time
import os
#import other a library
try:
    import git
except:
    stream = os.popen('pip install GitPython')
    time.sleep(40)
finally:
    import git

def test():
    print("Hi from our_test()")
    print("i have to make it more effecient")
    repo = git.Repo(os.getcwd())
    current = repo.head.commit
    repo.remotes.origin.pull()
    if current != repo.head.commit:
                print("Git changed")
                print("Git changed")
                print("Git changed")
                print("Git changed")
                print("Git changed")
