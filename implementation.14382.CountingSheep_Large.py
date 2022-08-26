from sys import stdin
input = stdin.readline

template = "Case #{0}: {1}"

T = int(input())
for caseNum in range(1, T+1) :
    case = input().rstrip()
    if int(case) == 0 : 
        print(template.format(caseNum,"INSOMNIA"))
        continue
    multiple = case
    numbers = set()
    i = 2
    while True:
        for num in multiple :
            numbers.add(num)
        if len(numbers) == 10 :
            break
        multiple = str(int(case) * i)
        i+=1

    print(template.format(caseNum, multiple))
