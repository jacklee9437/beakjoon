from sys import stdin
input = stdin.readline

N = int(input())
stone = [list(map(int, input().split())) for _ in range(N)]

def check(r, c, n, m) :
    jewel = 0
    for i in range(r, r+n) :
        for j in range(c, c+m) :
            if stone[i][j] == 2 :
                jewel += 1
    return jewel

def cut(r, c, n, m, d) :
    chkrst = check(r, c, n, m)
    if chkrst == 1 :
        return (True, 1)
    elif chkrst == 0 :
        return (False, 0)
    

    count = 0
    for i in range(r if d else r+1, r+n if d else r+n-1) :
        for j in range(c+1 if d else c, c+m-1 if d else c+m) :
            if stone[i][j] == 1 :
                if d == 0 :
                    for k in range(c, c+m) :
                        if stone[i][k] == 2 :
                            break
                    else :
                        up, upcnt = cut(r, c, i-r, m, d^1)
                        dn, dncnt = cut(i+1, c, r+n-i-1, m, d^1) if up else (False, 0)
                        if up and dn :
                            count += upcnt * dncnt
                else :
                    for k in range(r, r+n) :
                        if stone[k][j] == 2 :
                            break
                    else :
                        left, lcnt = cut(r, c, n, j-c, d^1)
                        right, rcnt = cut(r, j+1, n, c+m-j-1, d^1) if left else (False, 0)
                        if left and right :
                            count += lcnt * rcnt
    if count == 0:
        return (False, 0)
    else :
        return (True, count)

answer = 0
chkrst = check(0, 0, N, N)
if chkrst == 1 :
    answer = 1
elif chkrst == 0 :
    pass
else :
    for i in range(N) :
        for j in range(N) :
            if stone[i][j] == 1 :
                if 0 < i < N-1 :
                    for k in range(N) :
                        if stone[i][k] == 2 :
                            break
                    else :
                        able1, cnt1 = cut(0, 0, i, N, 1)
                        able2, cnt2 = cut(i+1, 0, N-i-1, N, 1) if able1 else (False, 0)
                        if able1 and able2 :
                            answer += cnt1 * cnt2
                if 0 < j < N-1 :
                    for k in range(N) :
                        if stone[k][j] == 2 :
                            break
                    else :
                        able1, cnt1 = cut(0, 0, N, j, 0)
                        able2, cnt2 = cut(0, j+1, N, N-j-1, 0) if able1 else (False, 0)
                        if able1 and able2 :
                            answer += cnt1 * cnt2
print(answer if answer else -1)