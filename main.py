import time
import os

while True:
    try:
        stream = os.popen('python pulllfile.pyw')
        if(stream.read()==''):
            stream = os.popen('python3 pulllfile.pyw')
        print(type(stream.read()))
    except:
        print("error found in main block")
    finally:
        print("finally from main")
        
    
    time.sleep(20)
