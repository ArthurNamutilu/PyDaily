#Decorators - function that takes a function as input & returns a modified version of that function.

def decfunc(f):
	def wrapper():
		print("Start")
		f()
		print("Stop")
	return wrapper


@decfunc
def sayhi():
	print("Use of decorators in python")


sayhi()
