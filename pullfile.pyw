#deafult python library import
import os
import time

from tasklist1 import test
#import a library
try:
    import requests
except:
    stream = os.popen('pip install requests')
    time.sleep(40)
finally:
    import requests
    
#import your library library


#define as many as task as a function then call it from main 
def othertask():
    dir_name="Abba Tanim"
    try: 
        os.makedirs(f'C:\\Users\\{os.getlogin()}\\Desktop\\{dir_name}')
    except OSError as error: 
        os.removedirs(f'C:\\Users\\{os.getlogin()}\\Desktop\\{dir_name}') 



def main():
    test()
    othertask()

if __name__ == "__main__":
    main()
