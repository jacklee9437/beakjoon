'''
https://velog.io/@redcarrot01/ProblemSolving-1939-%EC%A4%91%EB%9F%89%EC%A0%9C%ED%95%9C-BFS-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89-%ED%81%AC%EB%A3%A8%EC%8A%A4%EC%B9%BC
이분탐색 버전 참고

아이디어 
- 탐색해야하는 범위가 너무 넓기때문에 일단 bfs나 다익스트라로는 시간초과 나기가 쉬움. 따라서 이분탐색을 고려해볼 필요가 있음.
- 가능한 범위 내에서 이분탐색, 가정은 '이분탐색하려고 정한 mid값을 최소로하는, 출발지에서 도착지로가는 경로가 있다'
- 즉, mid값보다 작은 경로로 가서 발견이 안되면 False 반환하고 범위 좁혀서 탐색 지속
- mid값보다 큰 경로로 갔지만 발견이 안되면 동일하게 False 반환하고 범위 좁혀서 지속
- mid값보다 큰 경로로 가서 발견 되면 True 반환하고 mid를 높혀서 범위 줄여서 지속 - 값 저장
'''





# from heapq import heappop, heappush
# from sys import stdin
# input = stdin.readline

# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     A, B, C = map(int, input().split())
#     graph[A].append((B, C))
#     graph[B].append((A, C))
# P1, P2 = map(int, input().split())

# dist = [0] * (N+1)
# que = []
# heappush(que, (0, P1))

# while que:
#     ds, s = heappop(que)
#     if -ds < dist[s]:
#         continue
#     if s == P2:
#         break
#     for e, w in graph[s]:
#         d = w if not -ds else min(-ds, w)
#         if dist[e] < d:
#             dist[e] = d
#             heappush(que, (-d, e))

# print(dist[P2])
