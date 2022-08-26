from sys import stdin
input = stdin.readline

T = int(input())
cases = [input().rstrip() for _ in range(T)]

for idx, case in enumerate(cases, 1) :
    answer = ""
    i = 1

    for _ in range(len(case)) :
        while i < len(case) :
            if case[i-1] > case[i] :
                break
            i += 1
        else :
            answer = case
            break
        case = str(int(case[:i] + "0" * (len(case) - i)) - 1)
        i = 1
    
    print(f"Case #{idx}: {answer}")