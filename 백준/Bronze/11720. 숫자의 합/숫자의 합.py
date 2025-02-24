import sys
input = sys.stdin.readline

n = int(input())
stringList = list(input())
newList = []

for i in range(n):
  newList.append(int(stringList[i]))

print(sum(newList))