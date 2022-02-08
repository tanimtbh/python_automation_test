#deafult python library import
import os
import time

#import other task from tasklist1.py and tasklist2.py
from tasklist1 import otherTask
#from tasklist2 import task1, task2


#import a library


# try:
#     import requests
# except:
#     stream = os.popen('pip install requests')
#     time.sleep(40)
# finally:
#     import requests  



#import your library library
try:
    import git
except:
    stream = os.popen('pip install GitPython')
    time.sleep(40)
finally:
    import git




def selfInject():
    print("Hi selfInject() git")
    repo = git.Repo(os.getcwd())
    current = repo.head.commit
    repo.remotes.origin.pull()
    if current != repo.head.commit:
                print("Git changed")
                print("Git changed")
                print("Git changed")
                print("Git changed")
                print("Git changed")




#define as many as task as a function then call it from main 


def main(): # invoke the imported function here
    selfInject() 
    #bellow add your tasks
    otherTask()

if __name__ == "__main__":
    main()
