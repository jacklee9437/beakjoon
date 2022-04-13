from collections import deque
from sys import maxsize, stdin
input = stdin.readline

N = int(input())
circlesCR = [tuple(map(int,input().split())) for _ in range(N)]
circlesLR = []

for C, R in circlesCR :
    xL = C - R
    xR = C + R
    circlesLR.append((xL,xR))

circlesLR.sort(reverse=True, key= lambda x:x[1])
circlesLR.sort(key = lambda x:x[0])

stk = deque()
areaCnt = 1

for circle in circlesLR :
    if stk and stk[-1]["x"][1] <= circle[0] :
        temp = 0
        while stk and stk[-1]["x"][1] <= circle[0] :
            # print(stk, areaCnt)
            temp = stk.pop()
            if temp["is-linked"] :
                if stk and stk[-1]["x"][1] == temp["x"][1] :
                    stk[-1]["is-devided"] = True
            areaCnt += 2 if temp["is-devided"] else 1
        stk.append({"x":circle, "is-devided":False, "is-linked":True if temp["x"][1] == circle[0] else False})
    else :
        stk.append({"x":circle, "is-devided":False, "is-linked":True if stk and stk[-1]["x"][0] == circle[0] else False})

while stk :
    # print(stk, areaCnt)
    temp = stk.pop()
    if temp["is-linked"] :
        if stk and stk[-1]["x"][1] == temp["x"][1] :
            stk[-1]["is-devided"] = True
    areaCnt += 2 if temp["is-devided"] else 1

print(areaCnt)


'''
큰원을 열고
- 다음원을 보는데 일단 큰 원 안에 있는지 확인
-- 밖에 있으면 이전 원 닫는데, 내부 연결되어있었는지 확인 (스택에 넣을때 전달해서 넣기)
-- 안에 있으면 왼쪽에 닿는지 확인
--- 왼쪽에 닿으면 이전 원에 대해서 연결되어있었다고 체크하고 다음원 확인
--- 안닿으면 스택에 넣고 다음 원 확인
-- ...
- 스택이 얼마나 쌓였냐가 원을 얼마나 열었냐의 의미가 됨.



답은 잘 나오는데 백준에서 틀렸다고 나옴.
반례 찾기 여려움.

일단 기본 개념이, 괄호와 같이 일단 넣고 닫힐때 계산을 하는 방식이기 때문에 개념은 맞음.

'''




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