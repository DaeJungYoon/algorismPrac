import sys
input = sys.stdin.readline

n = int(input())

scoreList= list(map(int,input().split()))
maxScore = max(scoreList)

newList= []
  
for score in scoreList:
  newList.append(score/maxScore*100)

avg = sum(newList)/n
print(avg)