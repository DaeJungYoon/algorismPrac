# import sys
# input = sys.stdin.readline

# # n,m=map(int,input().split())

# # result = []



# # for i in range(n):
# #   result.append(i+1)
# # # print(first)
# # for _ in range(m):
# #   i,j=map(int, input().split())
# #   # print(first[i-1])
# #   # print(first[j-1])
# #   result.insert(j,result.pop(i-1))
# #   result.insert(i,result.pop(j-1))
# #   # result.insert(1,result.pop(0))
# #   # result.insert(2,result.pop(1))
# #   # result.insert(3,result.pop(2))
# #   # result.insert(4,result.pop(3))

# # print(*result)
# result2 = [1,2,3,4,5]
# result2.insert(1,result2.pop(0))
# result2.insert(2,result2.pop(1))
# print(*result2)


# list_ = [1,2,3]
# list_[0], list_[1] = list_[1],list_[0]
# print(list_)
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

result= []

for i in range(n):
  result.append(i+1)

for _ in range(m):
  i, j = map(int,input().split())
  result[i-1],result[j-1] = result[j-1],result[i-1]

print(*result)