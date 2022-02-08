from concurrent.futures import ThreadPoolExecutor
import time
import os
from myTelegram import patialMain


def tasks():
    while True:
        try:
            if os.name in ('nt', 'dos'):
                stream = os.popen('python pullfile.pyw')
            else:
                stream = os.popen('python3 pullfile.pyw')
                print(stream.read())
        except:
            print("error found in main->tasks block")
        finally:
            print("finally from main working")
        
        time.sleep(20)
        


def main():
    print("Starting ThreadPoolExecutor")
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(tasks)
        future = executor.submit(patialMain)

    print("All tasks complete")
    print(future)

if __name__ == '__main__':
    main()