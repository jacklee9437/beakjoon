from sys import maxsize, stdin
input = stdin.readline

def isContact(presC,compC) :
    xDiff = presC[0] - compC[0]
    if xDiff == presC[1] + compC[1]  : 
        return ("lo", presC[0] - presC[1])
    elif xDiff == presC[1] - compC[1] : 
        return ("li", presC[0] - presC[1])
    elif -xDiff == presC[1] + compC[1]  :
        return ("ro", presC[0] + presC[1])
    elif -xDiff == presC[1] - compC[1] :
        return ("ri", presC[0] + presC[1])
    return False

N = int(input())
circles = [tuple(map(int,input().split())) for _ in range(N)]

lineCntLeft = [0] * N
lineCntRight = [0] * N
contacts = set()

circles.sort()

for i in range(N-1) :
    for j in range(i+1,N) :
        if lineCntLeft[i] and lineCntRight[i] :
            break
        temp = isContact(circles[i],circles[j])
        # print(i,j,temp)
        if temp and temp[0][0] == "l" :
            if temp[0][1] == "i" :
                lineCntLeft[i] = lineCntLeft[j] = 1
            elif temp[0][1] == "o" :
                lineCntLeft[i] = lineCntRight[j] = 1
            contacts.add(temp[1])
        elif temp and temp[0][0] == "r" :
            if temp[0][1] == "i" :
                lineCntRight[i] = lineCntRight[j] = 1
            if temp[0][1] == "o" :
                lineCntRight[i] = lineCntLeft[j] = 1
            contacts.add(temp[1])
        
        
v = len(contacts)
e = 0
for k in range(N) :
    if lineCntLeft[k] and lineCntRight[k] :
        e += 2
    else : e += 1
f = 2-v+e
# print(lineCntLeft)
# print(lineCntRight)
print(f)



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

실패원인
1. 시간초과
2. 오일러지표가... 왜...

반례 :
5
2 2
1 1
3 1
8 3
12 1

오일러지표를 정확히 이해하지 못한 부분,,
https://velog.io/@phw1996/Python-%EB%B0%B1%EC%A4%80-10000%EB%B2%88-%EC%9B%90-%EC%98%81%EC%97%AD-%ED%92%80%EC%9D%B4

오일러지표를 사용해서 문제 풀려면 v,e도 예외적으로 다르게 생각해주어야하고,
v-e+f=2로 상수가 고정적인게 아니라 컴포넌트 c 값을 구해야하므로 유니온 파인드 알고리즘 이란걸 적용해야함.
나중에 추가로 공부하기로 하고 이번엔 패스...
-----


'''