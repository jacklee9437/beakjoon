from copy import deepcopy
from sys import stdin, setrecursionlimit, maxsize
input = stdin.readline

setrecursionlimit(10**6)

N, M = map(int,input().split()) # N 행수, M 열수
iceberg = [list(map(int,input().split())) for _ in range(N)]

G = [list() for _ in range(N*M+1)]

def dfs(n) :
    stk = []
    stk.append(n)
    while stk :
        temp = stk.pop()
        visit[temp] = True
        for i in G[temp] :
            if not visit[i] :
                stk.append(i)

def chkmelt() :
    for i in range(N) :
        for j in range(M) :
            if iceberg[i][j] != 0 :
                return False
    return True

tempIceberg = deepcopy(iceberg)
years = 0
while True :
    if chkmelt() :
        print(0)
        exit()
    for i in range(1, N-1) :
        for j in range(1, M-1) :
            if iceberg[i][j] != 0 :
                cnt = 0
                if iceberg[i+1][j] != 0 :
                    G[M*i+j].append(M*(i+1)+j)
                    cnt += 1
                if iceberg[i][j+1] != 0 :
                    G[M*i+j].append(M*i+j+1)
                    cnt += 1
                if iceberg[i-1][j] != 0 :
                    G[M*i+j].append(M*(i-1)+j)
                    cnt += 1
                if iceberg[i][j-1] != 0 :
                    G[M*i+j].append(M*i+j-1)
                    cnt += 1
                tempIceberg[i][j] = iceberg[i][j] - (4-cnt) if iceberg[i][j] > 4-cnt else 0
    
    cntV = 0
    visit = [False] * (N*M+1)
    if years > 0 :
        for v in range(1, N-1) :
            for u in range(1, M-1) :
                if not visit[v*M + u] and iceberg[v][u] :
                    
                    dfs(v*M + u)
                    cntV +=1
                    if cntV > 1 :
                        print(years)
                        exit()
    years += 1
    iceberg = deepcopy(tempIceberg)
    G = [list() for _ in range(N*M+1)]



'''
내 생각 :
0까지 다 저장할 필요가 없는게, 어차피 4-연결된노드수 가 바다 개수가 됨.
그래서 애초에 0 빼고 나머지를 데이터 정리 해서 그래프 연결리스트 형태로 저장해주고,
DFS해주면서 1년후의 연결리스트/빙산높이 를 구해줌.
이거를 반복다가 dfs 횟수가 여러번이 되면 그때의 횟수 출력
문제점 - 노드의 개수가 달라지는뎀...
0이 되면 노드 없음, 0 넘을땐 주변에 남아있을 노드 확인해서 연결리스트 생성,,,

연결리스트 만들어서 dfs 돌리면 오래걸림...
그냥 어차피 상하좌우만 연결된거니까 따로 연결리스트 만들지 말고,
상하좌우 확인해서 0 아닌것만 방문하도록 하면 됨...
https://codinghack.tistory.com/67

'''
























# 그래프 DFS

# # 입력
# N = int(input())
# A = input().rstrip()
# opersCnt = list(map(int,input().split()))
# opers = []

# nodes = [list() for _ in range(N+1)]
# for _ in range(N-1) :
#     u,v = map(int,input().split())
#     nodes[u].append(v)
#     nodes[v].append(u)

# # 재귀방법
# def dfs(s, v=1) : 
#     global cnt
#     chkvisit[s] = True
#     if v!=1 and A[s]=='1' :
#         cnt += 1
#         return
#     for i in nodes[s] :
#         if not chkvisit[i] :
#             dfs(i, v+1)

# chkvisit = [False] * (N+1)
# for i in range(1,N+1) :
#     if chkvisit[i] == False :
#         dfs(i)