# Бхаргава А. Грокаем алгоритмы

def binary_search(list, item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high)
		gues = list[mid]

		if gues == item:
			return mid

		if gues > item:
			high = mid - 1
		else:
			low = mid + 1

	return None

if __name__ == '__main__':
	my_lis = [1, 3, 5, 7, 9]

	print(binary_search(my_lis, 7))  
	print(binary_search(my_lis, -1))  
