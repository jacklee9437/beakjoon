from re import A
from sys import stdin
input = stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int,input().split()))
sensors.sort()

lengths = [sensors[i+1] - sensors[i] for i in range(N - 1)]
lengths.sort()

for _ in range(K-1) :
   if lengths :
      lengths.pop()

print(sum(lengths))