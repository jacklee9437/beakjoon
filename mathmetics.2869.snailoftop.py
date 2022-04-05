from math import ceil
from sys import stdin
input = stdin.readline

a,b,v = map(int,input().split())

day = ceil((v-b)/(a-b))
print(day)