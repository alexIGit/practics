def sum_two_ints(a: int, b:int) -> int:
  return a + b


def print_sum(a:int, b:int) -> None:
  print(sum_two_ints(a, b))


if __name__ == "__main__":
  #1
  print('result is: ', print_sum(10, 20))

