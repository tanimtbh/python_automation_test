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
    def clearConsole():
        command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

    clearConsole()