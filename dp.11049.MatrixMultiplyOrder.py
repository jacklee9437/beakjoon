from sys import stdin, maxsize
input = stdin.readline

N = int(input())
RCs = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(1, N) :
    for j in range(0, N-i) :

        if i == 1 :
            dp[j][j+1] = RCs[j][0] * RCs[j][1] * RCs[j+1][1]
            continue

        dp[j][j+i] = maxsize
        for k in range(j, j+i) :
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + RCs[j][0] * RCs[k][1] * RCs[j+i][1])

print(dp[0][N-1])


'''
dp 2차원 배열은 생각했지만, 너무 가짓수가 많을 것 같고 다 기록을 못할 것 같아서 해맸음.
dp에 기록해야하는거는 항상 중복된 계산이 발생하는 부분임. 즉, 부분적인 계산을 모두 기록해야하는 것은 아니었음.
그리고 테이블의 목적을 제대로 정의할 필요가 있음.
이 경우에는, 행에서 열까지 곱셈을 진행했을때의 최소횟수를 기록한다고 정했으면 좀 더 접근할 수 있었음!
'''