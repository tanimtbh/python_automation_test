import time


while True:
    try:
        from our_test import test
        test()
        del test
    except:
        print("Something wrong")
    finally:
        print("finally from main")
        
    
    time.sleep(20)
    