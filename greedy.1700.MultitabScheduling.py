from sys import stdin, maxsize
input = stdin.readline

N, K = map(int,input().split())
things = list(map(int,input().split()))

pluged = set()
cnt = 0

for idx, thing in enumerate(things) :
    if len(pluged) < N :
        pluged.add(thing)
        continue

    if thing in pluged :
        continue

    temp = (0, 0)
    for p in pluged :
        if p not in things[idx:] :
            temp = (p,)
            break
        found = things[idx:].index(p)
        if temp[1] < found :
            temp = (p, found)
    pluged.discard(temp[0])
    pluged.add(thing)
    cnt += 1

print(cnt)