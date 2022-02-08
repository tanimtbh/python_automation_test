#deafult python library import
# import os
# import time

#import other task from tasklist1.py and tasklist2.py
from tasklist1 import otherTask
from tasklist2 import task1, task2

def main(): # invoke the imported function here
    #bellow add your tasks
    otherTask()
    task1()
    task2()

if __name__ == "__main__":
    main()
