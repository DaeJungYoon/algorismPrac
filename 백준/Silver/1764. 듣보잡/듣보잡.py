import sys
input=sys.stdin.readline

n,m = map(int,input().split())
names={}

for _ in range(n+m):
  name = input().rstrip()
  if name in names:
    names[name] +=1
  else:
    names[name] =1

result = []

for name, counts in names.items():
  if counts == 2:
    result.append(name)

result.sort()

print(len(result))
print(*result, sep="\n")
