from sys import stdin, setrecursionlimit, maxsize
input = stdin.readline
INF = maxsize
setrecursionlimit(10000)

M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

dp = [[-1] * N for _ in range(M)]


def dfs(r=0, c=0):
    if dp[r][c] != -1:
        return dp[r][c]
    if r == M-1 and c == N-1:
        return 1
    val = 0
    for v in range(4):
        nr = r + dr[v]
        nc = c + dc[v]
        if 0 <= nr < M and 0 <= nc < N:
            if Map[nr][nc] < Map[r][c]:
                val += dfs(nr, nc)
    dp[r][c] = val
    return dp[r][c]


print(dfs())

# 성공했지만, dp를 0으로 초기화해서 방문했다가 경로가 없는경우 방문처리가 안됨.
# 해당 경우 예외처리를 하는라 코드가 복잡해짐. 애초에 dp를 0이외의 값으로 초기화하면 해결됨.
# def dfs(r=0, c=0):
#     if dp[r][c]:
#         return dp[r][c]
#     if r == M-1 and c == N-1:
#         return 1
#     val = 0
#     for v in range(4):
#         nr = r + dr[v]
#         nc = c + dc[v]
#         if 0 <= nr < M and 0 <= nc < N:
#             if Map[nr][nc] < Map[r][c]:
#                 temp = dfs(nr, nc)
#                 val += temp if temp != INF else 0
#     if val == 0:
#         dp[r][c] = INF
#         return dp[r][c]
#     dp[r][c] = val
#     return dp[r][c]
