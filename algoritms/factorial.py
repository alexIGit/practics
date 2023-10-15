

def factorial(n:int):
	assert n >= 0, "Факториал отрицательного числа неопределён"

	if n == 0:
		return 1

	return factorial(n-1) * n


if __name__ == "__main__":

	print(factorial(5)) 
	print(factorial(0)) 
	print(factorial(-5)) 
