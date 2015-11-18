def solve(A, B, N):
  i = 0
  while i < N:
    if A[i] == 0 and B[i] == 0:
      A[i] = 1
      B[i] = 1
    if A[i] == 0 and B[i] == 1:
      if i == N - 1:
        return "NO"
      if A[i + 1] == 1:
        return "NO"
      A[i + 1] = 1
      A[i] = 1
    if A[i] == 1 and B[i] == 0:
      if i == N - 1:
        return "NO"
      if A[i + 1] != 1:
        A[i + 1] = 1
        B[i] = 1
      else:
        if B[i + 1] != 1:
          B[i + 1] = 1
          B[i] = 1
        else:
          return "NO"
    i += 1
  return "YES"
T = input()
for i in range(T):
  N = input()
  A = [int(x) for x in raw_input()]
  B = [int(x) for x in raw_input()]
  print solve(A, B, N)