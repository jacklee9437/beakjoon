from sys import stdin, maxsize
input = stdin.readline

for _ in range(int(input())) :
    N = int(input())
    applicants = [list(map(int,input().split())) for _ in range(N)]

    applicants.sort()

    ans = 1
    end = applicants[0][1]
    
    for a, b in applicants[1:] :
        if b < end :
            ans += 1
            end = b

    print(ans)