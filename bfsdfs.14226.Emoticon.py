from collections import deque
from sys import stdin
input = stdin.readline

S = int(input())

checked = set()

que = deque()
que.append((1, 0, 0))

while que :
    display, clipboard, stopwatch = que.popleft()
    if display == S :
        print(stopwatch)
        break

    if (display, clipboard) in checked :
        continue 
    checked.add((display, clipboard))

    for i in range(3) :
        if i == 0 :
            que.append((display, display, stopwatch+1))
        elif i == 1 :
            if clipboard :
                que.append((display+clipboard, clipboard, stopwatch+1))
        else :
            if display :
                que.append((display-1, clipboard, stopwatch+1))

