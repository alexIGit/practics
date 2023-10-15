"""Проверка равенства строк."""

def equal(A, B):
  if len(A) != len(B):
    return False

  for i in range(len(A)):
    if A[i] != B[i]:
      return False

  return True



if __name__ == "__main__":

  A = "moloko"
  B = "moloto"
  C = "molotok"
  D = "molotok"

  print(A, B, "\tis equal: ", equal(A, B))
  print(A, C, "\tis equal: ", equal(A, C))
  print(C, D, "\tis equal: ", equal(C, D))
