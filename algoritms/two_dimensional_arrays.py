"""
  Реализация двумерного массива на питоне.
"""

#
# def method_1(N, M):
#   """
#     Линеаризация массива.
#     N - количество строк
#     M - количество элементов в строке
#   """
#
#   A[i][j] = A[i * (M + j)]
#   return A
#

def method_2(N, M):
  """
    Неправильный метод
  """
  A = [[0] * M] * N
  return A

def method_3(N, M):

  A = [[0] * M for i in range(N)]
  return A


if __name__ == "__main__":
  A1 = method_2(3, 3)
  A2 = method_3(3, 3)

  print(A1)
  print(A2)

  A1[0][0] = 99
  A2[0][0] = 99

  print(A1)
  print(A2)

  print(A1[0] is A1[1])
  print(A2[0] is A2[1])
