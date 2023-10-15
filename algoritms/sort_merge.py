


def merge(A:list, B:list):
	"""Слияние 2-х отсортированных массивов"""

	C = [0] * (len(A) + len(B))
	# print(C)

	i = k = n = 0

	while i < len(A) and k < len(B):
		if A[i] < B[k]:
			C[n] = A[i]
			i += 1
			n += 1
		else:
			C[n] = B[k]
			k += 1
			n += 1

	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1

	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1

	return C




		

def merge_sort(A:list):
	"""рекувсивная сортировка списка A методом слияния

	асимптотика: O(N log N)

	сортирующее действие выполняется на обратном ходу

	нужно O(N) дополнительной памяти

	"""

	if len(A) <= 1:
		return

	middle = len(A) // 2

	L = [A[i] for i in range(0, middle)]
	R = [A[i] for i in range(middle, len(A))]

	merge_sort(L)
	merge_sort(R)

	C = merge(L, R)

	for i in range(len(A)):
		A[i] = C[i]

	

if __name__ == "__main__":
	from sort_test import sorting_test

	sorting_test(merge_sort) 
 
 
