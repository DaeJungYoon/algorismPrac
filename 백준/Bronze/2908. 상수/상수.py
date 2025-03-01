a, b = list(input().split())

newA = ''.join(reversed(a))
newB = ''.join(reversed(b))

if newA>newB:
  print(newA)
elif newA<newB:
  print(newB)