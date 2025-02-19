import sys
input=sys.stdin.readline

passList= []
passList2= []


for _ in range(28):
  a = int(input())
  passList.append(a)

for i in range(30):
  passList2.append(i+1)

resultList = list(set(passList2)-set(passList))
resultList.sort()


for i in resultList:
  print(i)