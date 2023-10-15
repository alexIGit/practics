



def count_sort(arr:list):
	""" сортировка списка arr методом подсчёта """
	
	scope = max(arr) + 1

	frequency_list = [0] * scope

	for x in arr:
		frequency_list[x] += 1


	arr[:] = []

	for number in range(scope):
		arr += [number] * frequency_list[number]



if __name__ == "__main__":
	from sort_test import sorting_test

	sorting_test(count_sort) 
 
 
