from collections import deque
from sys import stdin, maxsize
input = stdin.readline

N, K = map(int,input().split())

visit = [False] * (10**5+1)

que = deque()
que.append((N,0))

while que :
    cur, t = que.popleft()
    if cur == K :
        print(t)
        break
    case1 = cur - 1
    case2 = cur + 1
    case3 = cur * 2
    if case1 >= 0 and not visit[case1] :
        visit[case1] = True
        que.append((case1,t+1))
    if (case2 <= 10**5 and not visit[case2]) :
        visit[case2] = True
        que.append((case2,t+1))
    if (case3 <= 10**5 and not visit[case3]) :
        visit[case3] = True
        que.append((case3,t+1))
