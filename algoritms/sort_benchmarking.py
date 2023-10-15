

from benchmarking import execite_time


@execite_time
def benchmark_little_list(algoritm):
	print(algoritm.__name__, end="")

	arr = [4, 2, 5, 1, 3]
	algoritm(arr)


@execite_time
def benchmark_double_thousand_list(algoritm):
	print(algoritm.__name__, end="")

	arr = list(range(1, -(10**3), 3)) + list(range(0, 10**3))
	algoritm(arr)


@execite_time
def benchmark_millionare_list(algoritm):
	print(algoritm.__name__, end="")

	# arr = list(list(range(10**6, 1, 5))  + list(range(-10**3, 10**3, 2)))
	arr = list(range(10**4, 1, -1)) + [86, 45, 66]

	# print(arr[0:30])
	algoritm(arr)
	# print(arr[0:30])






if __name__ == "__main__":
	from sort_insert import insert_sort
	from sort_selection import selection_sort
	from sort_bubble import bubble_sort
	from sort_count import count_sort
	from sort_default import default_sort
	from sort_hoare_rec import hoare_sort
	from sort_merge import merge_sort






	benchmark_little_list(insert_sort)
	benchmark_little_list(selection_sort)
	benchmark_little_list(bubble_sort) 
	benchmark_little_list(count_sort) 
	benchmark_little_list(default_sort) 
	benchmark_little_list(merge_sort) 
	benchmark_little_list(hoare_sort) 

	print()

	benchmark_double_thousand_list(insert_sort)
	benchmark_double_thousand_list(selection_sort)
	benchmark_double_thousand_list(bubble_sort) 
	benchmark_double_thousand_list(count_sort) 
	benchmark_double_thousand_list(default_sort) 
	benchmark_double_thousand_list(merge_sort) 
	benchmark_double_thousand_list(hoare_sort) 


	print()

	# benchmark_millionare_list(insert_sort)
	# benchmark_millionare_list(selection_sort)
	# benchmark_millionare_list(bubble_sort) 
	# benchmark_millionare_list(count_sort) 
	benchmark_millionare_list(default_sort) 
	benchmark_millionare_list(merge_sort) 
	benchmark_millionare_list(hoare_sort) 
