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

def othertask():
    dir_name="Abba Tanim"
    try: 
        os.makedirs(f'C:\\Users\\{os.getlogin()}\\Desktop\\{dir_name}')
    except OSError as error: 
        os.removedirs(f'C:\\Users\\{os.getlogin()}\\Desktop\\{dir_name}') 

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
test()
othertask()
