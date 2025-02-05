import sys
input = sys.stdin.readline

totalPrice = int(input())
n = int(input())
itemList=[]

for _ in range(n):
  price, ea = map(int, input().split())
  resultPrice = price*ea
  itemList.append(resultPrice)

itemTotalPrice = sum(itemList)

if totalPrice == itemTotalPrice:
  print("Yes")
else:
  print("No")