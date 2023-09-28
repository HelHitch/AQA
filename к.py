
def wrapper(func):
		def inner():
				print(func.__name__)
				str_ = func().split()
				print(', '.join(str_))
				return ', '.join(str_)

		return inner()

@wrapper
def check():
		return 'Check print'
