from sys import stdin
input = stdin.readline

def dfs(case, ans, depth, k) :
    if depth == 6 :
        print(*ans)
        return
    for i in range(k) :
        ans.append(case[i])
        dfs(case[i+1:], ans, depth + 1, k-i-1)
        ans.pop()


while (case:= input().rstrip("\n")) != "0" :
    k, *S = case.split()
    dfs(S, [], 0, int(k))
    print()