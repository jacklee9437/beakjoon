from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.extend(B)
A.sort()
print(*A, sep=" ")