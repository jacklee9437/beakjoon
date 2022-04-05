from math import ceil
import time
from sys import stdin
input = stdin.readline

'''
-------- Concept --------
'''

# 확인 함수 (필요시)
def sort(nums) :
    # li = []
    while True :
        cnt_pass = 0
        for i in range(n-1) :
            if (nums[i] > nums[i+1]) :
                nums[i], nums[i+1] = nums[i+1], nums[i]
            else : 
                cnt_pass += 1
        if (cnt_pass == n - 1) : return nums

# 풀이 함수
def solve(nums : list) :
    nums = sort(nums)
    for num in nums :
        print(num)
    

if __name__ == "__main__" :

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

