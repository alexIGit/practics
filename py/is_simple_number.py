 
def is_simple_number(x):
	""" Определяет, является ли число простым.
		x - целое положительное число.
		Если простое, то возвращает True,
		а иначе - False
	"""
	divisor = 2
	while divisor < x:
		if x % divisor == 0:
			return False

		divisor += 1

	return True