# import sys
# input=sys.stdin.readline

# n,m = map(int,input().split())

# ballList=[]

# for _ in range(m):
#   i, j, k = map(int, input().split())

# # for j in range(j)


# for i in range(n):
#   ballList.append(i+1)

import sys
input=sys.stdin.readline

n,m = map(int, input().split())

basket = [0]*n

for l in range(m):
  i,j,k = map(int,input().split())
  for x in range(i,j+1):
    basket[x-1] = k

for x in range(n):
  print(basket[x], end=" ")
