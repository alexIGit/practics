
import time

from search_binary import binary_search
from search_simple import simple_search
from search_simple import array_search

def test_mode(function, element):
	my_list = [i for i in range(0, 10**6)]
	
	start_time = time.time()

	result = function(my_list, element)

	# print(result)

	end_time = time.time()
	execute_time = end_time - start_time


	print("%s. \tExecute time: %f. Result: %s" % (function.__name__, execute_time, result))



def test_not_found(function):
	element = -1
	test_mode(function, element)


def test_middle(function):
	element = 499546
	test_mode(function, element)

def test_big(function):
	element = 950123
	test_mode(function, element)

def test_very_big(function):
	element = 95012300
	test_mode(function, element)
	

if __name__ == "__main__":

	case = [test_not_found, test_middle, test_big, test_very_big]
	# case = [test_very_big]

	for test in case:
		print(test.__name__)
		test(binary_search)
		test(simple_search)
		test(array_search)
		print('\n')


