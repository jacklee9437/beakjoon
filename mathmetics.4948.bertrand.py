from math import trunc,sqrt
from sys import stdin
input = stdin.readline

def is_sosu_of(n) :
    if n == 1 : return False
    for i in range(2,trunc(sqrt(n))+1):
        if n%i == 0 : return False
    return True

cases = []
while True :
    case = int(input())
    if case == 0 : break
    cases.append(case)

for case in cases :
    cnt = 0
    for i in range(case+1,2*case+1) :
        if is_sosu_of(i) : cnt += 1
    print(cnt)
