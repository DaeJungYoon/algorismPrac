alphabet="abcdefghijklmnopqrstuvwxyz"

s = input()


for i in alphabet:
  if i in s:
    print(s.index(i), end=' ')
  else:
    print(-1,end=" ")
