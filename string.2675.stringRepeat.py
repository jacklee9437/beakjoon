import sys

t = int(sys.stdin.readline())
for i in range(t):
    r, s = sys.stdin.readline().split()
    for char in s :
        print(char * int(r), end="")
    print()