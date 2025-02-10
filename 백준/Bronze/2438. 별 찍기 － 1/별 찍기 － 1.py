import sys
input = sys.stdin.readline

t = int(input())
stars = []

for _ in range(t):
  stars.append("*")
  print(*stars,sep="")