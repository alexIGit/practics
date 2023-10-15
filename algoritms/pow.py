
def pow(a:float, n:int):
	"""Быстрое возведение в степень"""
	if n == 0:
		return 1

	else:
		return pow(a, n - 1) * a


def pow_even(a:float, n:int):
	"""Быстрое возведение в степень
	если n-чётная
	"""
	if n == 0:
		return 1

	elif n % 2 == 1: # нечётное
		return pow_even(a, n - 1) * a

	else:
		return pow_even(a ** 2, n // 2) 


if __name__ == "__main__" :
	print(pow(3, 2))
	print(pow(5, 5))
	print(pow(2, 10), end='\n\n')

	print(pow_even(3, 2))
	print(pow_even(5, 5))
	print(pow_even(2, 10))
