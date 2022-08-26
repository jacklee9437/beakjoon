from sys import stdin
input = stdin.readline

N = int(input())
bitmask = [0] * (N+1)
perms = []

def permutations(depth, li) :
    global N
    if depth == N :
        print(*li)
        return

    for i in range(1, N+1) :
        if not bitmask[i] :
            bitmask[i] = 1
            li.append(i)
            permutations(depth + 1, li)
            li.pop()
            bitmask[i] = 0

permutations(0, [])