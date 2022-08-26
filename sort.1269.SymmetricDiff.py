from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
A = set(input().split())
B = set(input().split())
answer = len((A-B) | (B-A))
print(answer)
