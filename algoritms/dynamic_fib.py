# from benchmarking import execite_time

# @execite_time


def fib(number):
  if number <= 1:
    return number

  return fib(number - 1) + fib(number - 2)


# Dynamic

def fib_dyn(n):
  arr = [0, 1] + [0] * (n - 1)

  for i in range(2, n + 1):
    arr[i] = arr[i - 1] + arr[i - 2]

  return arr[n]


if __name__ == "__main__":
  # from benchmarking import execite_time

  import time

  num = 35

  start_time = time.time()
  fib_num = fib(num)
  end_time = time.time()
  execute_time = end_time - start_time

  start_time = time.time()
  fib_num_dyn = fib_dyn(num)
  end_time = time.time()
  execute_time_dyn = end_time - start_time

  print("\tExecute time simple fib %d:  %f. Result: %d" % (num, execute_time, fib_num))
  print("\tExecute time dynam. fib %d:  %f. Result: %d" % (num, execute_time_dyn, fib_num_dyn))
