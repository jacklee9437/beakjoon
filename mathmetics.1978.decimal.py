from math import ceil, sqrt
from sys import stdin
input = stdin.readline



n = int(input())
nums = list(map(int,input().split()))

cnt = 0

for num in nums:
    result = True
    if (int(sqrt(num)) < 2) :
        if (num == 1) :
            result = False
    else :
        for i in range(2, int(sqrt(num)) + 1) :
            if (num%i == 0) :
                result = False
                break
    if result == True :
        cnt += 1

print(cnt)