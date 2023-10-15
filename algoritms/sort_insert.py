



def insert_sort(arr:list):
	""" сортировка списка arr вставками """
	
	N = len(arr)

	for top in range(1, N):
		k = top

		while k > 0 and arr[k-1] > arr[k]:
			arr[k], arr[k-1] = arr[k-1], arr[k]
			k -= 1


if __name__ == "__main__":
	from sort_test import sorting_test

	sorting_test(insert_sort) 
