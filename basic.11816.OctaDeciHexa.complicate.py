from sys import stdin
input = stdin.readline

numbers = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "a" : 10, "b" : 11, "c" : 12, "d" : 13, "e" : 14, "f" : 15}

X = input().rstrip()
ans = 0
if X[:2] == "0x" :
    for idx, val in enumerate(reversed(X[2:])) :
        ans += numbers[val] * (16 ** idx)
elif X[:1] == "0" :
    for idx, val in enumerate(reversed(X[1:])) :
        ans += numbers[val] * (8 ** idx)
else :
    ans = int(X)

print(ans)