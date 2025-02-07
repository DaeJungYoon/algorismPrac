import sys
input = sys.stdin.readline

n = int(input())

count = n//4

types = []

for _ in range(count):
  types.append("long")

types.append("int")

print(*types)

