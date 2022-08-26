from sys import stdin
input = stdin.readline

N = int(input())
tmpN = N
for i in range(2, N+1) :
    while tmpN % i == 0 :
        print(i)
        tmpN //= i
