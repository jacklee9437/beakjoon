from sys import stdin
input = stdin.readline

string = input().rstrip()
bumb = list(input().rstrip())


stk = []

for c in string :
    stk.append(c)
    if c == bumb[-1] :
        if stk[-len(bumb):] == bumb :
            for _ in range(len(bumb)) :
                stk.pop()
            
print("FRULA" if not stk else ''.join(stk))