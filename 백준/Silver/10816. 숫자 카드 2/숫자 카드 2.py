import sys 
input = sys.stdin.readline

result = {}
n = int(input())
nums=map(int,input().split())

for _ in range(n):
  for num in nums:
    if num in result:
      result[num] += 1
    else:
      result[num] = 1

m = int(input())
nums2=map(int,input().split())

result2=[]
for _ in range(m):
  for num in nums2:
    result2.append(result.get(num,0))

print(*result2)

      



