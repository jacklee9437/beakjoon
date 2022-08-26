from operator import truediv
from sys import stdin
input = stdin.readline

N = int(input())
cards = set(map(int,input().split()))

M = int(input())
check = list(map(int,input().split()))

ans = [1 if i in cards else 0 for i in check]
print(*ans)