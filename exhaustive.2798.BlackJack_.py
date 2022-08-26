from itertools import combinations
from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
cards = map(int,input().split())

answer = 0
cases = list(combinations(cards, 3))
for case in cases :
    s = sum(case) 
    if s <= M :
        answer = max(answer, s)