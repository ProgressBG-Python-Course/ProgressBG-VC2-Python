def stars_decorator(f):
	def wrapper():
		print("*" * 50)
		f()
		print("*" * 50)

	return wrapper

# let's decorate greet:
@stars_decorator
def greet():
	print("Howdy World!")

# and use it:
greet()