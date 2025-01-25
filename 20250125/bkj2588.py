import sys
input = sys.stdin.readline

num1=int(input())
num2=int(input())

print(num1*(num2 % 10))
print(num1*(num2 % 100 // 10))
print(num1*(num2 % 1000 //100))
print(num1*num2)