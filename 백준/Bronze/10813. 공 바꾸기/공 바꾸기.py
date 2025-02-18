import sys
input = sys.stdin.readline

n,m = map(int, input().split())

result= []

for i in range(n):
  result.append(i+1)

for _ in range(m):
  i, j = map(int,input().split())
  result[i-1],result[j-1] = result[j-1],result[i-1]

print(*result)