import time


while True:
    try:
        from our_test import test
    except:
        print("Something wrong")
    finally:
        test()
        print("finally from main")
        
    
    time.sleep(20)
    del test