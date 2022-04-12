from collections import deque
from sys import maxsize, stdin
input = stdin.readline

N = int(input())
circles = [tuple(map(int,input().split())) for _ in range(N)]

lr_circles = []
for circle in circles :
    l = circle[0] - circle[1]
    r = circle[0] + circle[1]
    lr_circles.append((l,r))
lr_circles.sort(reverse=True, key= lambda x: x[1])
lr_circles.sort(key= lambda x: x[0])
# print(lr_circles)

stk = deque()
# contacts = set()

for circle in lr_circles :
    if not stk :
        stk.append(circle)
        # print(circle, stk)
        continue

    if stk[-1][0] == circle[0] :
        contacts.add(circle[0])
        stk.append(circle)
    elif stk[-1][0] < circle[0] < stk[-1][1] :
        stk.append(circle)
    elif circle[1] == stk[-1][1] :
        contacts.add(circle[1])
        stk.append(circle)
    else :
        if stk[-1][1] == circle[0] :
            contacts.add(circle[0])
        while stk and stk[-1][1] <= circle[0] :
            temp = stk.pop()
            if stk and temp[1] == stk[-1][1] :
                contacts.add(temp[1])
            if temp[0] in contacts and temp[1] in contacts :
                e += 2
            else :
                e += 1
        stk.append(circle)
    print(circle, stk, e, contacts)

while stk :
    temp = stk.pop()
    if stk and temp[0] < stk[-1][1] :
        if temp[1] == stk[-1][1] :
            contacts.add(temp[1])
        if temp[0] in contacts and temp[1] in contacts :
            e += 2
        else :
            e += 1
    else : 
        if temp[0] in contacts and temp[1] in contacts :
            e += 2
        else :
            e += 1

    


print(ans)



'''
🤔🤔🤔 문제정의를 잘 하자 🤔🤔🤔

입력 : 원의 개수 N, 원의 정보 x,r
출력 : 원으로 인해 만들어지는 영역의 수

찾아야하는 값 : 오일러지표 v-e+f=1 에 따라, f=1-v+e. ans = f + 1. 즉, 꼭지졈과 변의 수만 구하면 됨. 
알고리즘 : 정렬(일단 왼쪽부터 확인하려면 정렬 필요한듯), 자료구조, 스택(스택을 어떻게 써먹을까...), 오일러지표

-----
접하는 원이 없거나 원이 하나만 접하면 일단 접점은 한개.
원이 양쪽으로 접하면 점이 두개.

원 한개당 변은 1개 또는 두개. 접점이 1개면 1개, 2개면 두개.

스캔하면서 확인해야할 내용
- 원의 왼/오 좌표
- 하나의 원에 대해 접하는 원이 있는지, 몇개있는지


-----


'''