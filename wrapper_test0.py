import time

def timeit(func):
	def wrapper():
		start=time.clock()
		func()
		end=time.clock()
		print ('time:',end-start)
	return wrapper
@timeit
def foo():
	print ('in foo()')
foo()
