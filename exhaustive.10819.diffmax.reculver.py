from itertools import permutations
import time
from sys import stdin
input = stdin.readline

'''
-------- Concept --------
순열 & 재귀 사용한 버전
- 순열을 재귀적으로 구현하는 것도 가능 (bit map 사용)
- abs의 합을 재귀적으로도 구현 가능
'''


# 필요한 함수
def sum_of(arr, n):
    if n > 1 :
        return sum_of(arr,n-1) + abs(arr[n-2] - arr[n-1])
    else :
        return 0


if __name__ == "__main__":

    # 입력
    n = int(input())
    a = list(map(int, input().split()))

    # 풀이시작전 기록
    # start = time.time()

    # 문제 풀이
    perms = list(permutations(a))
    maximum = 0
    for perm in perms :
        _max = sum_of(perm, n)
        if (_max > maximum) :
            maximum = _max
        
    print(maximum)

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")
