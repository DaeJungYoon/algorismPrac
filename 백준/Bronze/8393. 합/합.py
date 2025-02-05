import sys
input = sys.stdin.readline

n = int(input())

first = 0
nums =[]
for __ in range(n):
  first +=1
  # print(first)
  nums.append(first)
  
print(sum(nums))