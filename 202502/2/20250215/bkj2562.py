import sys
input=sys.stdin.readline

numList = []

maxNum = float("-inf")

for _ in range(9):
  a = int(input())
  numList.append(a)

for i in range(9):
  if numList[i] > maxNum:
    maxNum = numList[i]

print(maxNum)
print(numList.index(maxNum)+1)
