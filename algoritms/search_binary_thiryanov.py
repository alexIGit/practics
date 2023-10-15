from search_test import test_array_search


def left_bound(A, key):
	# print(A)
	# print(key)
	left = -1
	right = len(A)



	while right - left > 1:
		middle = (left + right) // 2



		if A[middle] < key:
			left = middle

		else:
			right = middle


def right_bound(A, key):
	left = -1
	right = len(A)

	while right - left > 1:
		middle = (left + right) // 2

		if A[middle] <= key:
			left = middle

		else:
			right = middle

	return right



def binary_search(arr, element):
	left = left_bound(arr, element)
	# right = right_bound(arr, element)
	
	print(left)
	# print(right)

	return left


	

if __name__ == "__main__":

	test_array_search(binary_search)
 
