from sys import stdin, maxsize
input = stdin.readline

N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * (1<<N) for _ in range(N)] # dp[현재위치][bitmask] - 현재위치까지 bitmask 표시된대로 왔을 때, 뒷부분을 방문할 수 있는 모든 경우 중 최소값을 기록함.
MAX = maxsize

def go(now=0, visit=1) :
    if dp[now][visit] :
        return dp[now][visit] # 이미 기록한 적 있는 비트마스크이면 그 이후에 방문할 경로의 최소비용을 그냥 바로 리턴해줌
    if visit == (1<<N) - 1 :
        return W[now][0] if W[now][0] > 0 else MAX
    cost = MAX
    for i in range(1,N) :
        if not visit & (1<<i) and W[now][i] != 0 :
            val = go(i, visit | (1<<i))
            cost = min(cost, val + W[now][i]) # 뒤에 방문할 수 있는 모든 경우에서 최소비용을 갱신해줌
    
    dp[now][visit] = cost # now 까지 visit의 비트마스크처럼 방문한 경우 나머지를 방문하는 최소비용을 기록해줌
    return dp[now][visit]

print(go())

'''
이동하는 경로대로 최소를 기록한다고 생각하면 해당 경로를 중복방문하는 경우가 없어서 기록하는 의미가 없음.
하여 지금 dp에서 기록하고 있는 것은, 현재까지 어디까지 방문했다면 그 이후에 방문할 수 있는 모든 경우의 수에서 최소 비용을 구한 값임.
즉, 어떤 순서로 방문해서 왔든지간에 현재까지 방문한 위치가 동일하다면, 그 뒤에 방문해야하는 위치들도 동일하기 때문에 뒤에 방문하는 경우의 최소비용을 기록하는 것.
그래야 뒤에서 다른 순서로 오더라도 방문한 위치만 같으면 이미 계산된 값을 가져와서 쓸 수 있는 것!

여기서 깨닫는 점은, dp는 어찌보면 깊이우선으로 저장해줘야한다,,
상향식이더라도 낮은 단계부터 올라가고 있음!
깊이 들어가는 부분에서 반복이 발생하는것이기 때문에...!
'''