


%%time
def bubble_sort(arr:list):
	""" сортировка списка arr методом пузырька """
	
	N = len(arr)

	for bypass in range(1, N):
		for k in range(0, N - bypass):
			if arr[k] > arr[k+1]:
				arr[k], arr[k+1] = arr[k+1], arr[k]


if __name__ == "__main__":
	from sort_test import sorting_test

	sorting_test(bubble_sort) 
 
 
