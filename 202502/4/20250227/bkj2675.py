# import sys
# input=sys.stdin.readline

# n = int(input())

# for i in range(n):
#   r,s=map(str,input().split())
#   r=int(r)
#   s=list(s)
#   for j in range(len(s)):
#     print(s[j]*r, end='')

# print('')


Case = int(input())

for i in range(Case):
    N, S = input().split()
    for j in range(len(S)):
        print(S[j] * int(N), end = '')
    print('')