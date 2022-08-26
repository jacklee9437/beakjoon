from operator import truediv
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())

graph = []
for _ in range(M) :
   a, b, c = map(int,input().split())
   graph.append((c, a, b))
graph.sort()

parent = list(range(N+1))

def find(c) :
   if parent[c] != c :
      parent[c] = find(parent[c])
      return parent[c]
   else :
      return c

def union(c1, c2) :
   if find(c1) != find(c2) :
      parent[parent[c1]] = parent[c2]
      return True
   return False

cost = 0
for c, a, b in graph :
   if union(b, a) :
      cost += c

print(cost)
