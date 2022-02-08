from concurrent.futures import ThreadPoolExecutor
import threading
import time
import os

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
            print("finally from main")
        
        time.sleep(20)
        
def communitcations():
    test=20
    while True:
        test=test+1
        print("test value: ", test)
        print("Task Executed {}".format(threading.current_thread()))
        time.sleep(20)
        if(test==15):
            break



def main():
    print("Starting ThreadPoolExecutor")
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(tasks)
        future = executor.submit(communitcations)

    print("All tasks complete")
    print(future)

if __name__ == '__main__':
    main()