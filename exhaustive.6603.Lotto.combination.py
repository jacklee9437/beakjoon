from itertools import combinations
from sys import stdin
input = stdin.readline

while (case:= input().rstrip("\n")) != "0" :
    k, *S = case.split()
    combi = list(combinations(S, 6))
    [print(' '.join(map(str,sorted(map(int,x))))) for x in combi]
    print()