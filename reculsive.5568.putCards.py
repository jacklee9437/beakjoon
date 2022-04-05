from ast import AsyncFunctionDef
import time
from sys import stdin
input = stdin.readline

# 확인 함수 (필요시)
def recur(k) :
    if (k == 0) :
        s.add(''.join(li))
        return
    for i in range(n) :
        if (chk_card[i] == 1) :
            continue
        chk_card[i] = 1
        li.append(cards[i])
        recur(k-1)
        chk_card[i] = 0
        li.pop()

        

# 풀이 함수
def solve(k) :
    recur(k)
    print(len(s))



if __name__ == "__main__" :

    # 입력
    n = int(input())
    k = int(input())
    cards = [input().strip() for _ in range(n)]
    li, s = [], set()
    chk_card = [0] * n

    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    solve(k)
    

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {end - start:.5f} sec")

