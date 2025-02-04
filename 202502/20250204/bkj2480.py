a, b, c =map(int,input().split())

# if 같은 눈이 3개 나오면:
#   print(10000 + a * 1000)
# elif 같은 눈이 2개 나오면:
#   print(1000 + 같은 눈 * 100)
# elif a>b and a>c:
#   print(a * 100)
# elif b>c and b>a:
#   print(b * 100)
# elif c>a and c>b:
#   print(c * 100)

if a == b and b==c:
  print(10000 + a * 1000)
elif b==a or a==c:
  print(1000 + a * 100)
elif a==b or b==c:
  print(1000 + b * 100)
elif a==c or c==b:
  print(1000 + c * 100)
elif a>b and a>c:
  print(a * 100)
elif b>c and b>a:
  print(b * 100)
elif c>a and c>b:
  print(c * 100)
  