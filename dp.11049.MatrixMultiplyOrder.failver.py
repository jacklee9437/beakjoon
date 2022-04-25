from sys import stdin
input = stdin.readline

N = int(input())
RCs = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * (N+1) for _ in range(N+1)]

# for i in range(2, N+1) :
#     r1, c1 = RCs[i-1]
#     r2, c2 = RCs[i]
#     val = r1 * c1 * c2
#     dp[2][i]

for i in range(2, N+1) :
    for j in range(i, N+1) :
        case1 = dp[i-1][j-1] + RCs[j-i+1][0] * RCs[j][0] * RCs[j][1]
        case2 = dp[i-1][j] + RCs[j-i+1][0] * RCs[j-i+1][1] * RCs[j][1]
        dp[i][j] = min(case1, case2)

        # print('---------------')
        # print("case1 : %d, case2 : %d"%(case1,case2))
        # print("dp[%d][%d] = %d"%(i,j,dp[i][j]))

# print(*dp,sep="\n")
print(dp[N][N])


'''
좋은 접근이었을지 모르겠으나 실패.
왜냐,, 이 경우에는 2개 먼저 구하고 이를 바탕으로 3개, 4개 ,, 구해나가지만 계속 한단계를 바탕으로 구하는 오류를 범함.
즉, 4개의 경우, 2개 * 2개 로 묶은 경우도 있는데 이부분이 포함되지 않음.
행이 증가할때마다 아래 행들의 모든 경우를 생각할 수도 있겠으나, 경우가 계속 증가함....

'''