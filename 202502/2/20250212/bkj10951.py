import sys
input = sys.stdin.readline

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

# 계속 반복 해서 a, b 인풋을 받는다.
# 근데 들어오는 인풋이 없으면?
# 멈추고 a+b 값을 출력한다
# or
# 계속 반복 해서 a, b 인풋을 받는다.
# 그리고 받은 인풋을 빈 리스트에 넣는다
# 빈 리스트에 넣을때는 [[a,b], [a,b]]
# 형태로 넣고
# [a,b] 리스트의 합하고 
# 다른 빈 리스트의 값을 넣고
# 넣은 리스트의 요소들을 모두 출력한다
# resultList =[]
# while True:
#   a,b = map(int,input().split())
#   sortList=[a,b]
#   resultList.append(sum(sortList))
#   continue
# print(resultList)