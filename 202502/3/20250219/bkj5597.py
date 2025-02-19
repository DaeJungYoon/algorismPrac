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
# for i in passList:
#   for j in range(len(passList)):
#     if i != a:
#       result.append(j)
# print(result)
# for i in range(27):
#   if passList[i] != i+1:
#     result.append(passList[i])

# print(result)

# 28줄의 인풋을 받아
# 배열에 넣어주고
# 그 배열의 요소들을 쭉 탐색하여
# 그 요소와 인데스+1이 같으면