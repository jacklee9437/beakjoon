import sys


def sum_of(a):
    sum = 0
    cnt = 0
    for i in range(len(a)):
        if (a[i] == "O"):
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    return sum


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [sys.stdin.readline() for i in range(n)]

    for i in arr:
        print(sum_of(i))

