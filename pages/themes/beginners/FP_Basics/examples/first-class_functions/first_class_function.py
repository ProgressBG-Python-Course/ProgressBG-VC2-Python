

#a function can be assigned to variable:
# foo = greet
# greet("Maria")
# foo("Pesho")

# a function can be passed as argument to another function
# def wrapper(f, n):
# 	f(n)

# wrapper(greet, "Alex")

#a function can be returned as value from another function
def greet_wrapper(name):
	def wrapper():
		print("Hello, {}".format(name))

	return wrapper

foo = greet_wrapper("Viktor")
foo()
