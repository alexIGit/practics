
from search_test import test_array_search

def binary_search(arr, element):
	mid = len(arr) // 2
	low = 0
	high = len(arr) - 1

	while arr[mid] != element and low <= high:
	    if element > arr[mid]:
	        low = mid + 1
	    else:
	        high = mid - 1
	    mid = (low + high) // 2

	if low > high:
	    return -1
	else:
	    return mid




	

if __name__ == "__main__":

	test_array_search(binary_search)



