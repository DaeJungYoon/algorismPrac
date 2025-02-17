import sys
input = sys.stdin.readline

n,m = map(int, input().split())

result = [0]*n

for _ in range(m):
  i,j,k = map(int, input().split())
  for x in range(i-1,j):
    result[x] = k



print(*result)