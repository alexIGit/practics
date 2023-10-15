



def hoare_sort(A:list):
	"""рекувсивная сортировка списка A методом Хоара

	асимптотика: W(N log N), O(N**2)

	сортирующее действие выполняется на прямом ходу

	без дополнительной памяти

	разделяй и властвуй
	"""
	
	if len(A) <= 1:
		return

	barrier = A[0]

	L = []
	M = []
	R = []

	for x in A:
		if x < barrier:
			L.append(x)

		elif x == barrier:
			M.append(x)

		else:
			R.append(x)

	hoare_sort(L)
	hoare_sort(R)

	k = 0

	for x in L + M + R:
		A[k] = x
		k += 1




if __name__ == "__main__":
	from sort_test import sorting_test

	sorting_test(hoare_sort) 
 
 
