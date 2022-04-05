from math import ceil, sqrt
import time
from sys import stdin
input = stdin.readline

def is_sosu_of(n) :
    result = True
    if (int(sqrt(n)) < 2) :
        if (n == 1) :
            result = False
    else :
        for i in range(2, int(sqrt(n)) + 1) :
            if (n%i == 0) :
                result = False
                break
    return True if result == True else False

def solve(case) :
    for i in range(int(case/2), 1, -1):
        a = i
        b = case - i
        if (is_sosu_of(a) and is_sosu_of(b)) :
            print("%d %d" %(a,b))
            break




if __name__ == "__main__" :

    # 입력
    t = int(input())
    cases = list(map(int,[input() for _ in range(t)]))


    # 풀이시작전 기록
    start = time.time()

    # 풀이 함수 실행
    for case in cases :
        solve(case)

    # 풀이 완료 기록 및 출력
    end = time.time()
    # print(f"소요시간 : {end - start:.5f} sec")

