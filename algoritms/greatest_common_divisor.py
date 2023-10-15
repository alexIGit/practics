
def gcd(a, b):
	"""Алгоритм Евклида
	Эффективный алгоритм для нахождения 
	наибольшего общего делителя двух целых чисел 

	"""

	if a == b:
		return a

	elif a > b:
		return gcd(a - b, b)

	else: # a < b
		return gcd(a, b - a)


def gcd1(a, b):
	"""алгоритм Евклида с помощью деления по модулю"""

	return a if b == 0 else gcd1(b, a % b)



if __name__ == "__main__":

	print(gcd(5, 5)) 
	print(gcd(6, 18)) 
	print(gcd(18, 6), end='\n\n') 

	print(gcd1(5, 5)) 
	print(gcd1(6, 18)) 
	print(gcd1(18, 6)) 
 
 
