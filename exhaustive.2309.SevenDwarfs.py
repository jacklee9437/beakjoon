import time
from sys import stdin
input = stdin.readline

'''
-------- Concept --------
백설공주와 일곱난쟁이
- 찐 난쟁이 7명의 키 합은 100임.
- 즉, 100을 넘는 키는 거짓말하는 2명 키의 합과 같음
- 완전 탐색하면서 두명의 키를 합쳤을 때 초과값이 되는 두명을 찾으면 됨
'''


# 필요한 함수
# def solve():


if __name__ == "__main__":

    # 입력
    heights = [int(input()) for _ in range(9)]

    # 풀이시작전 기록
    # start = time.time()

    # 문제 풀이
    sum_of_heights = sum(heights)
    liers_sum = sum_of_heights - 100
    heights.sort()
    is_found = False

    for i in range(8, 0, -1):
        for j in range(i-1, -1, -1):
            if (heights[i] + heights[j] == liers_sum):
                heights.remove(heights[i])
                heights.remove(heights[j])
                is_found = True
                break
        if is_found:
            break

    [print(i) for i in heights]

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")
