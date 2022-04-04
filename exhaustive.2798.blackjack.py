import time
from sys import stdin
input = stdin.readline

'''
-------- Concept --------
블랙잭
'''


# 필요한 함수
# def solve():


if __name__ == "__main__":

    # 입력
    n, m = map(int, input().split())
    cards = list(map(int, input().split())
    # cards = sorted(list(map(int, input().split())), reverse=True)

    # 풀이시작전 기록
    # start = time.time()

    # 문제 풀이
    sum=0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                _sum=cards[i] + cards[j] + cards[k]
                if (sum < _sum <= m):
                    sum=_sum
    print(sum)

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")
