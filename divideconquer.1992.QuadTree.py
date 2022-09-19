from sys import stdin
input = stdin.readline

N = int(input())
video = [input().strip() for _ in range(N)]


def prt(arr, n, p=(0, 0)):
    bi = arr[p[0]][p[1]]
    for i in range(p[0], p[0]+n):
        for j in range(p[1], p[1]+n):
            if arr[i][j] != bi:
                return "(" + prt(arr, n//2, (p[0], p[1])) + prt(arr, n//2, (p[0], p[1]+n//2)) + prt(arr, n//2, (p[0]+n//2, p[1])) + prt(arr, n//2, (p[0]+n//2, p[1]+n//2)) + ")"
    return bi


print(prt(video, N))
