from collections import defaultdict, deque
from sys import stdin
input = stdin.readline

N = int(input())
Graph = defaultdict(list)
# 최대 흐를 수 있는 유량
Capacity = defaultdict(lambda : defaultdict(int))
for _ in range(N) :
    a, b, c = input().split()
    c = int(c)
    # 유량상쇄를 위해 양방향으로 등록
    Graph[a].append(b)
    Graph[b].append(a)
    # 유량상쇄시 무의미한 값이 최소값이 되지 않을 수 있도록 양방향으로 유량 등록
    Capacity[a][b] += c
    Capacity[b][a] += c

# 실제 유량
Flow = defaultdict(lambda : defaultdict(int))
minFlow = float('inf')
result = 0

while True :
    # visited 역할. A부터 Z까지 가는 경로를 저장
    route = defaultdict(str)
    que = deque(["A"])
    while que :
        fv = que.popleft()
        if fv == "Z" :
            break

        for tv in Graph[fv] :
            if tv == "A" : continue
            if not route[tv] and Capacity[fv][tv] - Flow[fv][tv] > 0 :
                route[tv] = fv
                que.append(tv)
    # 한바퀴 돌았으나 Z로 못도달하는 경우 흐르지 못한다는 의미이므로 break
    if not route["Z"] :
        break
    
    # 되돌아가면서 최소 유량 (흐를 수 있는 최대 유량) 찾기
    v = "Z"
    while route[v] :
        minFlow = min(minFlow, Capacity[route[v]][v]-Flow[route[v]][v])
        v = route[v]
    
    # 찾은 최소 유량으로 Flow 갱신 - 유량상쇄를 위해 반대로는 -로 흐르도록 저장
    v = "Z"
    while route[v] :
        Flow[route[v]][v] += minFlow
        Flow[v][route[v]] -= minFlow
        v = route[v]
    
    # 누적
    result += minFlow
    minFlow = float('inf')

print(result)