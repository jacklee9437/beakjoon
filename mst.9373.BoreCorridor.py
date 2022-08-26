from sys import stdin
input = stdin.readline

def distanceBetweenTwoCircles(a, b) :
    xa, ya, ra = a
    xb, yb, rb = b
    distance = (abs(xa - xb) ** 2 + abs(ya - yb) ** 2) ** 0.5
    return distance - ra - rb

def distanceBetweenWallAndCircle(c, w) :
    xc, yc, rc = c
    lw = xc-rc
    rw = w - (xc+rc)
    return max(lw, rw)

T = int(input())

for _ in range(T) :
    w = int(input())
    n = int(input())
    sensors = [list(map(int, input().split())) for _ in range(n)]
    sensors.sort(key=lambda x:x[1])

    dist = distanceBetweenWallAndCircle(sensors[0], w)
    
    for i in range(1, n) :
        dist = min(dist,min(distanceBetweenTwoCircles(sensors[i-1], sensors[i]), distanceBetweenWallAndCircle(sensors[i], w)))

    if dist < 0 :
        print(0)
    else :
        dist = round(dist/2, 6)
        print(dist)





    # parent = list(range(n))

    # def find(c) :
    #     if parent[c] != c :
    #         parent[c] = find(parent[c])
    #         return parent[c]
    #     return c

    # def union(c1, c2) :
    #     if find(c1) != find(c2) :
    #         parent[parent[c1]] = parent[c2]
    #         return True
    #     return False
