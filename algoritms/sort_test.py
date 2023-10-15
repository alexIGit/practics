


def sorting_test(sort_algoritm):
	print("Тестируем: ", sort_algoritm.__doc__)

	print("testcase #1: ", end="")
	arr = [4, 2, 5, 1, 3]
	arr_sorted = [1, 2, 3, 4, 5]

	sort_algoritm(arr)
	print("Ok" if arr == arr_sorted else "Fail")
	
	

	print("testcase #2: ", end="")
	arr = list(range(10, 20)) + list(range(0, 10))
	arr_sorted = list(range(0, 20))

	sort_algoritm(arr)
	print("Ok" if arr == arr_sorted else "Fail")


	print("testcase #3: ", end="")
	arr = [4, 2, 4, 2, 1]
	arr_sorted = [1, 2, 2, 4, 4]

	sort_algoritm(arr)
	print("Ok" if arr == arr_sorted else "Fail")


if __name__ == "__main__":
	from sort_insert import insert_sort
	from sort_selection import selection_sort
	from sort_bubble import bubble_sort
	from sort_count import count_sort
	from sort_default import default_sort






	sorting_test(insert_sort)
	sorting_test(selection_sort)
	sorting_test(bubble_sort)
	sorting_test(count_sort)
	sorting_test(default_sort)


