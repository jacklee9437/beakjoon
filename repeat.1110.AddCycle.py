from sys import stdin
input = stdin.readline


N = int(input())

new_N = 0
cycle = 0

a = N//10
b = N % 10
c = a+b
new_N = b*10 + c%10
cycle += 1

while new_N != N:
    a = new_N//10
    b = new_N % 10
    c = a+b
    new_N = b*10 + c%10
    cycle += 1

print(cycle)
