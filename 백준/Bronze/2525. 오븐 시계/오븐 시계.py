h, m =map(int,input().split())
requireM = int(input())

endTimeH = h
endTimeM = m+requireM

while endTimeM>=60:
  endTimeH+=1
  endTimeM -=60
if endTimeH>=24:
  endTimeH -=24
print(endTimeH,endTimeM)
