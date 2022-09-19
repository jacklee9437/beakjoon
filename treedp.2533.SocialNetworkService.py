from sys import stdin, setrecursionlimit
setrecursionlimit(int(1e9))
input = stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

def dfs(node) :
    visited[node] = 1
    for child in graph[node] :
        if not visited[child] :
            dfs(child)
            dp[node][1] += min(dp[child][0], dp[child][1])
            dp[node][0] += dp[child][1]
    dp[node][1] += 1

dfs(1)
print(min(dp[1][1], dp[1][0]))