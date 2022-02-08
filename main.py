import time
import os

while True:
    try:
        if os.name in ('nt', 'dos'):
            stream = os.popen('python pullfile.pyw')
        else:
            stream = os.popen('python3 pullfile.pyw')
        print(stream.read())
    except:
        print("error found in main block")
    finally:
        print("finally from main")
        
    time.sleep(60)
