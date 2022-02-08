#deafult python library import
import os

#import other a library
# try:
#     import git
# except:
#     stream = os.popen('pip install GitPython')
#     time.sleep(40)
# finally:
#     import git

def otherTask():
    dir_name="We are not Slave"
    try: 
        os.makedirs(f'C:\\Users\\{os.getlogin()}\\Desktop\\{dir_name}')
    except OSError as error: 
        os.removedirs(f'C:\\Users\\{os.getlogin()}\\Desktop\\{dir_name}') 

