from concurrent.futures import ThreadPoolExecutor
import threading
import time



def taska(test):
    while True:
        test=test+1
        print("test value taska: ", test)
        print("Task Executed {}".format(threading.current_thread()))
        time.sleep(3)
        if(test==15):
            break
    
def task(test):
    while True:
        test=test+1
        print("test value: ", test)
        print("Task Executed {}".format(threading.current_thread()))
        time.sleep(3)
        if(test==15):
            break

def task(n):
 print("Processing {}".format(n))

def main():
 print("Starting ThreadPoolExecutor")
 with ThreadPoolExecutor(max_workers=3) as executor:
   future = executor.submit(taska, (0))
   future = executor.submit(task, (3))

 print("All tasks complete")
 print(future)

if __name__ == '__main__':
 main()