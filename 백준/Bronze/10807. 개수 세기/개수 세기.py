import sys
input = sys.stdin.readline

t = int(input())


nums=map(int,input().split())

a = int(input())

intList = []

count = 0

for num in nums: 
  intList.append(num)

for i in range(t):
  if intList[i] == a:
    count += 1

print(count)