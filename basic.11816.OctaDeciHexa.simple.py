from sys import stdin
input = stdin.readline

X = input().rstrip()
if X[:2] == "0x" :
    print(int(X, 16))
elif X[:1] == "0" :
    print(int(X, 8))
else :
    print(int(X))