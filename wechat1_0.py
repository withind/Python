import time
def foo():
    start = time.clock()
    print ('in foo()')
    end = time.clock()
    print ('used:', end - start)
 
foo()
