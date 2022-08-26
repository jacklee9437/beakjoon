from sys import stdin
input = stdin.readline

T = int(input())
if T % 10 :
    print(-1)
    exit(0)

buttons = [300, 60, 10]
val = T
for i in range(3) :
    print("%d"%(val//buttons[i]), end=" ")
    val %= buttons[i]
