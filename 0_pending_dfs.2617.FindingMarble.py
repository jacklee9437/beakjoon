from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
dsc = [set() for _ in range(N+1)]
asc = [set() for _ in range(N+1)]
for _ in range(M) :
    heavy, light = map(int,input().split())
    dsc[heavy].add(light)
    asc[light].add(heavy)

def dfs(start) :
    stk = []
    dscCnt = 0
    ascCnt = 0
    chked = [False] * (N+1)
    stk.append(start)
    while stk :
        s = stk.pop()
        chked[s] = True
        for i in dsc[s] :
            if not chked[i] :
                dscCnt += 1
                stk.append(i)
    chked = [False] * (N+1)
    stk.append(start)
    while stk :
        s = stk.pop()
        chked[s] = True
        for i in asc[s] :
            if not chked[i] :
                ascCnt += 1
                stk.append(i)
    print("%d보다 무거운건 %d개 / 가벼운건 %d개" %(start,ascCnt,dscCnt))
    return max(ascCnt, dscCnt)

cnt = 0
for i in range(1, N+1) :
    temp = dfs(i)
    if N // 2 < temp :
        cnt += 1
print(cnt)


# 일단 큰순서 작은순서대로 각각 구한거 최대값 구한다음에 중간보다 넘으면 중간일 가능성 없는걸로 해보는데
# 시간초과 날 가능성 높음
# 시간초과 난다면, 그냥 dfs 하면서 기존에 있는 애들 말고 다른애들이 생기면 기존꺼에 추가하는 방식도 고려가능.. 하지만 이것도 오래걸리긴 마찬가지일듯.

# 웨않뒈