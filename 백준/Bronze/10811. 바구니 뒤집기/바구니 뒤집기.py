import sys 
input = sys.stdin.readline

baskets = []
temp = 0
n, m = map(int,input().split())

for i in range(n):
  baskets.append(i+1)

for _ in range(m):
  i,j=map(int,input().split())
  temp=baskets[i-1:j]
  temp.reverse()
  baskets[i-1:j] = temp


print(*baskets)