from sys import stdin
input = stdin.readline


def cnt_of(n):
    global count
    if n == 0:
        count += 1
    else:
        for i in range(1, 4):
            if n-i >= 0:
                cnt_of(n-i)
# comment : 점화식 개념으로 재귀를 사용하려면 count를 return 하도록 구현하면 좋을 것 같다.


T = int(input())
cases = tuple(int(input()) for _ in range(T))

for case in cases:
    count = 0
    cnt_of(case)
    print(count)
