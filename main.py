import time
import os

while True:
    try:
        stream = os.popen('python our_test.py')
        print(stream.read())
    except:
        stream = os.popen('python3 our_test.py')
    finally:
        print("finally from main")
        
    
    time.sleep(20)