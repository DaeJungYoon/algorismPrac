import sys
input = sys.stdin.readline

n,x = map(int,input().split())

nums = map(int,input().split())

newNums = []

result=[]

for num in nums:
  newNums.append(num)

for i in range(n):
  if newNums[i]<x:
    result.append(newNums[i])

print(*result)