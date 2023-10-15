
def test_array_search(search_function):
	arr1=[1, 2, 3, 4, 5]
	n = search_function(arr1, 8)

	print('\n', search_function.__name__)

	if n == -1:
		print("#test1 - ok")
	else:
		print("#test1 - fail")


	arr2 = [-1, -2, -3, -4, -5]
	n = search_function(arr2, -3)

	if n == 2:
		print("#test2 - ok")
	else:
		print("#test2 - fail")

	arr3 = [10, 20, 30, 10, 11]
	n = search_function(arr3, 10)

	if n == 0:
		print("#test3 - ok")
	else:
		print("#test3 - fail") 

	arr4 = [1, 3, 3, 3, 7, 9]
	n = search_function(arr4, 3)

	if n == 1:
		print("#test4 - ok")
	else:
		print("#test4 - fail") 

if __name__ == "__main__":
	from search_binary import binary_search
	from search_simple import simple_search
	from search_simple import array_search

	test_array_search(binary_search)
	test_array_search(simple_search)
	test_array_search(array_search)


