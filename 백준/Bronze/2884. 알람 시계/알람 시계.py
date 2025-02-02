h, m =map(int,input().split())

alarmHour = h
alarmMinute= m-45

if alarmMinute <0:
  alarmHour-=1
  alarmMinute+=60
if alarmHour <0:
  alarmHour +=24

print(alarmHour, alarmMinute)
