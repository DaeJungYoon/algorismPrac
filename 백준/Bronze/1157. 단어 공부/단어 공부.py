arr=list(map(str.upper,input()))

result = {}

for i in arr:
  if i in result:
    result[i] += 1
  else:
    result[i] = 1

maxValue = max(result.values())
maxkeys = [key for key, value in result.items() if value == maxValue]

if len(maxkeys) >1:
  print("?")
else:
  print(*maxkeys)