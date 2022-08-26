from collections import deque

for _ in range(int(input())) :
    n = int(input())
    adjList = [set() for _ in range(n+1)]
    indeg = [0] * (n+1)
    lastYear = list(map(int, input().split()))
    for i in range(n-1) :
        for j in range(i+1, n) :
            adjList[lastYear[i]].add(lastYear[j])
            indeg[lastYear[j]] += 1
    
    m = int(input())
    if m == 0 :
        print(' '.join(map(str, lastYear)))
        continue
    for _ in range(m) :
        a, b = map(int, input().split())
        if b in adjList[a] :
            adjList[a].remove(b)
            indeg[b] -= 1
            adjList[b].add(a)
            indeg[a] += 1
        else :
            adjList[b].remove(a)
            indeg[a] -= 1
            adjList[a].add(b)
            indeg[b] += 1
    
    que = deque()
    for i in range(1, n+1) :
        if indeg[i] == 0 :
            que.append(i)
    if not que :
        print("IMPOSSIBLE")
        continue

    ret = []
    flag = True
    while que :
        if len(que) > 1 :
            flag = False
        if not flag :
            break

        team = que.popleft()
        ret.append(team)
        for next in adjList[team] :
            indeg[next] -= 1
            if indeg[next] == 0 :
                que.append(next)
            elif indeg[next] < 0 :
                flag = False
                break
    
    if flag and len(ret) == n :
        print(*ret)
    else :
        print("IMPOSSIBLE")


