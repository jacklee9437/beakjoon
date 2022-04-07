import sys

x, y, w, h = map(int, sys.stdin.readline().split())
x = int(x)
y = int(y)
w = int(w)
h = int(h)

if (x < w-x) :
    if (y < h-y) :
        if (x < y) :
            print(x)
        else :
            print(y)
    else :
        if (x < h-y) :
            print(x)
        else :
            print(h-y)
else :
    if (y < h-y) :
        if (w-x < y) :
            print(w-x)
        else :
            print(y)
    else :
        if (w-x < h-y) :
            print(w-x)
        else :
            print(h-y)
