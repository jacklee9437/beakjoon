import sys

n, x = sys.stdin.readline().split()
a = sys.stdin.readline().split()
n = int(n)
x = int(x)

for i in a:
    i = int(i)
    if (i < x):
        print(i, end=" ")

