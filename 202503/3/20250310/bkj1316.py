n = int(input())

count = 0

for _ in range(n):
  word = list(input())
  newArr= []
  newArr.append(word[0]) 

  for i in range(len(word)-1):
    if newArr[-1] != word[i+1]:
      newArr.append(word[i+1])

  if len(newArr) == len(set(newArr)):
    count +=1

print(count)