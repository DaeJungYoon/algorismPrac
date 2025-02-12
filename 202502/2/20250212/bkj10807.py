import sys
input = sys.stdin.readline

t = int(input())


nums=map(int,input().split())

a = int(input())

intList = []

count = 0

for num in nums: 
  intList.append(num)

for i in range(t):
  if intList[i] == a:
    count += 1

print(count)
# 리스트 요소를 뽑아서 입력 받은 값 a와와 같으면 if intList[i]==a:
# 카운트 변수에 1추가 count += 1
# 카운트 변수 출력 print(count)
