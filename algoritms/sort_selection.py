



def selection_sort(arr:list):
	""" сортировка списка arr выбором """
	
	N = len(arr)

	for pos in range(0, N-1):
		for k in range(pos+1, N):
			if arr[k] < arr[pos]:
				arr[k], arr[pos] = arr[pos], arr[k]


if __name__ == "__main__":
	from sort_test import sorting_test

	sorting_test(selection_sort) 
 
