import time
from sys import stdin
input = stdin.readline

'''
-------- Concept --------
수의 범위가 작은 경우 카운팅 정렬 (도수 정렬) 사용해서 정렬하기
-> 자꾸 메모리 초과... -> 주어진 메모리 조건 하에서는 안정적인거 고려 안하고 풀어야 풀림.
'''


# 풀이 함수
# def dosu_sort():


# 실행 함수
# def solve():


if __name__ == "__main__":

    # 입력
    n = int(input())
    dosu = [0] * 10001

    for _ in range(n):
        dosu[int(input())] += 1

    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    for i in range(1, 10001):
        if dosu[i] != 0:
            for j in range(dosu[i]):
                print(i)

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")
