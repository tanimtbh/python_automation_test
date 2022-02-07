import time


while True:
    try:
        from our_test import test
        test()
        del test()
    except:
        print("Something wrong")
    finally:
        print("Yahoo from abba Tanim from finally a virsion changed again changed")
        
    
    time.sleep(20)
    