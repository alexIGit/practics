

from search_test import test_array_search

def simple_search(list, element):
	for index, value in enumerate(list):
		if value == element:
			return index 

	return -1


def array_search(arr:list, x:int):
	""" осуществляет поиск числа x в массиве arr
	от 0 до N-1 индекса включительно.
	Возвращает индекс элемента x в массиве arr.
	Или -1, если такого нет.
	Если в массиве несколько одинаковых элементов,
	равных x, то вернуть первого по счёту.

	"""

	for k in range(len(arr)-1):
		if arr[k] == x:
			return k
	

	return -1






if __name__ == "__main__":
	test_array_search(array_search)
	test_array_search(simple_search)
