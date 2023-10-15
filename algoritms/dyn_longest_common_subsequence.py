
def lcs(A, B):
  """ Longest common subsequence
  @param A: array of numbers
  @param B: array of numbers
  """

  N = len(A)
  M = len(B)

  F = [[0] *(M + 1) for i in range(N + 1)]
  for i in F: print(i)

  print(F)

  for i in range(1, (N+1)):
    for j in range(1, (M+1)):
      if A[i-1] == B[j-1]:
        F[i][j] = 1 + F[i-1][j-1]
      else:
        F[i][j] = max(F[i-1][j], F[i][j-1])

  for i in F: print(i)

  return F[-1][-1]






if __name__ == "__main__":

  A = [1, 2, 3, 4, 5, 6, 7, 0, 4, 5, 6, 7, 8, 9, 10]
  B = [4, 5, 6, 7, 8, 0, 4, 5, 6, 7, 8, 9, 10, 11]

  a_lcs = lcs(A, B)

  print(a_lcs)
