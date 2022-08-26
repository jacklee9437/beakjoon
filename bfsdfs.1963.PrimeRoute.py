from collections import deque
from math import sqrt
from sys import stdin
input = stdin.readline

# primeNumbers = set()
primeNumbers = [False] * 10000

# def setPrime(n) :
#     if n%2 == 0 : return
#     for i in range(3, int(sqrt(n))+1, 2) :
#         if n%i == 0 :
#             return
#     primeNumbers[n] = True
    # primeNumbers.add(n)

for n in range(1001, 9997, 2) :
    for i in range(3, int(sqrt(n))+1, 2) :
        if n%i == 0 :
            break
    else :
        primeNumbers[n] = True

T = int(input())
for _ in range(T) :
    start, end = input().split()
    if start == end :
        print(0)
        continue

    checked = set()
    checked.add(start)
    que = deque()
    que.append((start, 0))
    while que :
        prime, cnt = que.popleft()
        if prime == end :
            print(cnt)
            break
        for i in range(4) :
            listPrime = list(prime)
            for j in range(10) :
                listPrime[i] = str(j)
                tmpPrime = ''.join(listPrime)
                if not tmpPrime in checked and primeNumbers[int(tmpPrime)] :
                    checked.add(tmpPrime)
                    que.append((tmpPrime, cnt+1))
    else :
        print("Impossible")

