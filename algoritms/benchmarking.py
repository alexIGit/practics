
import time

def execite_time(executing_function) :

	def wrapper(*args, **kwargs):

		start_time = time.time()

		executing_function(*args, **kwargs)

		end_time = time.time()
		execute_time = end_time - start_time

		# return execute_time

		print("\t %s. \tExecute time: %f." % (executing_function.__name__, execute_time))

	return wrapper


