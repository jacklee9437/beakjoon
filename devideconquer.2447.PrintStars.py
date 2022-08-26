from sys import stdin
input = stdin.readline

N = int(input())
ans = []

def dnc(n, arr) :
    base = []
    if n == 3 :
        arr.extend(["***", "* *", "***"])
        return
    else :
        dnc(n//3, base)

    for i in range(3) :
        for star in base :
            str = ""
            for j in range(3) :
                if i == 1 and j == 1 :
                    str += " " * len(star)
                else :
                    str += star
            arr.append(str)

dnc(N, ans)
print(*ans, sep="\n")