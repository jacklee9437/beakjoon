from sys import stdin, maxsize
input = stdin.readline

N = int(input())
stair = [int(input()) for _ in range(N)] + [0]
stair.reverse()

dp = [0] * (N+1)
dp[1] = stair[1]

chk = True # 이전 계단에서 한계단 올랐는지 두계단 올랐는지 판단
for i in range(2,N+1) :
    if chk :
        dp[i] = max(dp[i-2] + stair[i], dp[i-1] + stair[i])
        if dp[i] == dp[i-1] + stair[i] :
            chk = False
    else :
        dp[i] = max(dp[i-2] + stair[i], dp[i-1])
        chk = True

print(*dp)
# print(max(dp[N], dp[N-1]))

'''
뒤에서 오면서 계속 최대값 갱신했더니 -> 안밟은거에도 최대값이 들어가있고, 뒤에서 다시 비교하게 되는데, 이때 안밟은게 밟은것처럼 되어버림.
그리고 처음엔 상관없는데 뒤에갔을때 연속 두번은 밟을 수 있는데 그걸 고려하지 못함.
'''