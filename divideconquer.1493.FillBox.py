from sys import stdin
input = stdin.readline

length, width, height = map(int, input().split())
N = int(input())
cubes = [list(map(int, input().split()))[1] for _ in range(N)]

minTotalCount = 0
filledArea = 0
for i in range(N-1, -1, -1) :
    size = 2 ** i
    filledArea *= 8

    needCount = (length // size) * (width // size) * (height // size) - filledArea
    realCount = min(needCount, cubes[i])

    minTotalCount += realCount
    filledArea += realCount

if filledArea == length * width * height :
    print(minTotalCount)
else :
    print(-1)