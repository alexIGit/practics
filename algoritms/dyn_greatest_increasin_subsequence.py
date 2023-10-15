
def gis(A):
  """ Greatest increasing subsequence
  @param A: array of numbers
  @param B: array of numbers
  """

  N = len(A)

  F = [0] * (N+1)


  # print(F)

  for i in range(1, (N+1)):

    m = 0
    for j in range(0, i):
      if A[i-1] > A[j-1] and F[j] > m:
        m = F[j]

      F[i] = m + 1

  print(A)
  print(F)

  return F[N]






if __name__ == "__main__":

  A = [-5, -3, -2, 0, 9, 2, 3, 4, 5, 6, 7, 0, 4, 5, 2, 6, 7, 8, 9, 10]

  a_gis = gis(A)

  print(a_gis)
