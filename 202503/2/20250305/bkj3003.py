a = list(map(int,input().split()))

intact = [1,1,2,2,2,8]

aList= []

result = []

for l in a:
  aList.append(l)

for i in range(len(intact)):
  resultNum = intact[i] - aList[i]
  result.append(resultNum)

print(*result)