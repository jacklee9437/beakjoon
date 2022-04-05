from itertools import permutations
import time
from sys import stdin
input = stdin.readline

'''
-------- Concept --------
재귀적으로? for 문으로? 순열로? 방문하는 순서 만들기

- 순열 
순열로 0~n-1까지 가능한 수열 만들기
순서대로 방문하는 비용의 합 구하기 [-1] ~ [-1] 까지
 => w[i][j] 로 구하되, 해당 값이 0인 경우는 예외처리 필요. 
 => sum에 계속 더한다음에 pay list에 추가하는 방법 or W[i][j]를 다른 리스트에 넣었다가 한번에 합 구하는 방법
 모든 순열에 대해 확인한 후 pay list의 최소값 출력
-> 시간초과,,, 중간에 최소값보다 커지면 바로 중단하고 나올 수 있도록 처리해야할듯
-> 오류발견. 출발지는 중요하지 않다! 왜냐면, 0 1 2 3 4 0 으로 돌아오나, 1 2 3 4 0 1 로 돌아오나 w[0][1] + w[1][2] + w[2][3] + w[3][4] + w[4][0] 인건 똑같음!


- 재귀
v를 1씩 올려가면서 v번째 방문
w[i][j] 구하려면 이전에 방문한 위치 필요 => 
방문했던 위치인지 확인 필요 => is_visited 비트 마스크
w[i][j]가 0인지 확인 필요
방문 가능한 위치이면 해당 w[i][j] 값을 global sum에 추가
v가 n에 도착하면 재귀 종결 - sum을 pay list에 추가, sum은 0으로 초기화
-> 답은 나오지만 시간초과
-> 출발지 고정하면 좋을듯!
'''


# 필요한 함수
def salesman(v) :
    global sum, mincost
    if v == 0 and all(is_visited) :
        mincost = sum
    else :
        for i in range(n) :
            if (is_visited[i] == 1) or (w[v][i] == 0) or ( mincost < sum + w[v][i] ) : continue
            sum += w[v][i]
            is_visited[i] = 1
            salesman(i)
            sum -= w[v][i]
            is_visited[i] = 0


if __name__ == "__main__":

    # 입력
    n = int(input())
    w = [list(map(int,input().split())) for _ in range(n)]

    # 풀이시작전 기록
    # start = time.time()

    # 문제 풀이
    is_visited = [0] * n
    mincost = pow(10,10)
    sum = 0

    salesman(0)
    print(mincost)

    
    

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")
