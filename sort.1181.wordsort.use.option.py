from re import L
import time
from sys import stdin
input = stdin.readline

'''
-------- Concept --------
단어 정렬하기
'''


# 풀이 함수
# def


# 실행 함수
# def solve():


if __name__ == "__main__":

    # 입력
    n = int(input())
    words = set()
    for _ in range(n):
        words.add(input().strip())

    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    words = list(words)
    words.sort()
    words.sort(key=len)
    [print(word) for word in words]

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")
