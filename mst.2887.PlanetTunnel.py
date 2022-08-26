from sys import stdin
input = stdin.readline

N = int(input())
planets = [tuple(map(int, input().split())) for _ in range(N)]

X = []
Y = []
Z = []

for i in range(N) :
   X.append((planets[i][0], i))
   Y.append((planets[i][1], i))
   Z.append((planets[i][2], i))

X.sort()
Y.sort()
Z.sort()

parent = list(range(N))

def find(child) :
   if parent[child] != child :
      parent[child] = find(parent[child])
      return parent[child]
   return child

def union(child1, child2) :
   if find(child1) != find(child2) :
      parent[parent[child1]] = parent[child2]
      return True
   return False

tunnels = []

for i in range(N-1) :
   tunnels.append((abs(X[i][0]-X[i+1][0]), X[i][1], X[i+1][1]))
   tunnels.append((abs(Y[i][0]-Y[i+1][0]), Y[i][1], Y[i+1][1]))
   tunnels.append((abs(Z[i][0]-Z[i+1][0]), Z[i][1], Z[i+1][1]))

tunnels.sort()

total = 0
for c, a, b in tunnels :
   if union(a, b) :
      total += c
      
print(total)
