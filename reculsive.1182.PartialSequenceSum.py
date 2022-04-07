from sys import stdin
input = stdin.readline


def cnt_of(i, sum=0):
    global N, S, count, nums
    if i < N:
        for idx in range(i, N):
            sum += nums[idx]
            if sum == S:
                count += 1
            cnt_of(idx+1, sum)
            sum -= nums[idx]


N, S = map(int, input().split())
nums = tuple(map(int, input().split()))

count = 0
cnt_of(0)

print(count)
