import sys
input = sys.stdin.readline

remainders = []
difCount = 0


for _ in range(10):
  num = int(input())
  remainders.append(num % 42)

result = set(remainders)

for _ in result:
  difCount += 1 

print(difCount)