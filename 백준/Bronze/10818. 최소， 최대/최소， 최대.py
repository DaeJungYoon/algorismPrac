import sys
input = sys.stdin.readline


t = int(input())

nums = map(int,input().split())

numList = []
resultList =[]

minNum = float("inf")
maxNum = float("-inf")

for num in nums:
  numList.append(num)

for i in range(t):
  if numList[i]<minNum:
    minNum = numList[i]
  if numList[i]>maxNum:
    maxNum = numList[i]
resultList.append(minNum)
resultList.append(maxNum)

print(*resultList)