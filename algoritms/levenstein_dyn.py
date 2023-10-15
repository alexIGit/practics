"""Расстояние Левенштейна."""

def levenstein(A, B):
  """
  Редакционное расстояние между строками.
  @param A:
  @param B:
  """

  F = [[i + j if i * j == 0 else 0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]

  # print(F)
  for i in F: print(i)

  for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
      if A[i-1] == B[j-1]:
        F[i][j] = F[i-1][j-1]
      else:
        F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])

  print("")
  for i in F: print(i)


  return F[len(A)][len(B)]



if __name__ == "__main__":
  A = "moloko"
  B = "kolokol"

  length = levenstein(A, B)

  print(length)
