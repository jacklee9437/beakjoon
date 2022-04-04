import time
from sys import stdin
from typing import Sequence
input = stdin.readline

'''
-------- Concept --------
Quick정렬, 병합정렬처럼 O(nlogn) 으로 나오는 방법을 적용해야함.
Quick 정렬 구현했으나 피벗을 배열의 중간위치로 정하다보니 최적의 시간복잡도가 나오지 않아 시간초과 발생.
중간값을 사용하여 피벗을 정하는 방식 써봐야할듯 하지만 지금단계에선 어려움. -> 일단 내장함수 사용하고 나중에 추가로 공부...
'''


# 풀이 함수

# 실행 함수


def solve(nums: list):
    result = sorted(nums)
    for num in result:
        print(num)


if __name__ == "__main__":

    # 입력
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    solve(nums)

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")
