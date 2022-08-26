from sys import stdin
input = stdin.readline

T = int(input())
A = 300
B = 60
C = 10

ans = []

if (T % C != 0) :
   ans.append(-1)
else :
   ans.append(T//A)
   T%=A
   ans.append(T//B)
   T%=B
   ans.append(T//C)

print(*ans)