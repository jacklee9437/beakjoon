import time
from sys import stdin
input = stdin.readline

'''
-------- Concept --------
'''


# 필요한 함수
# def solve():


if __name__ == "__main__":

    # 입력
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)

    # 풀이시작전 기록
    # start = time.time()

    # 문제 풀이
    new_arr = [0] * n
    for idx, val in enumerate(a):
        if (idx < n//2):
            new_arr[2 * idx + 1] = val
        else:
            new_arr[2 * (idx - n//2)] = val

    sum = 0
    for i in range(n-1):
        sum += abs(new_arr[i] - new_arr[i+1])

    print(new_arr)
    print(sum)

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")
