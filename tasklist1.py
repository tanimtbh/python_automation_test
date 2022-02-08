#deafult python library import
import time
import os
#import other a library

def otherTask():
    dir_name="Abba Tanim"
    try: 
        os.makedirs(f'C:\\Users\\{os.getlogin()}\\Desktop\\{dir_name}')
    except OSError as error: 
        os.removedirs(f'C:\\Users\\{os.getlogin()}\\Desktop\\{dir_name}') 

