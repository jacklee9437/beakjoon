from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
K = int(input())
Apps = [tuple(map(int,input().split())) for _ in range(K)]
L = int(input())
XCs = tuple(tuple(input().split()) for _ in range(L))

# 초기화
snake = deque()
r, c = 1, 1
snake.append((r,c))
t = 1
dirx = 0 # 우 - 하 - 좌 - 상 : 0 - 1 - 2 - 3
xcIdx = 0

# 벽이랑 부딪히는지 확인
def wallCrash(p,n) :
    if 0 < p[0] < n+1 and 0 < p[1] < n+1 :
        return False
    return True

# 자기 몸이랑 부딪히는지 확인
def selfCrash(s, p) :
    if p in list(s) :
        return True
    return False

# 벽이나 자기 몸이랑 부딪히는지 확인
def chkCrashed(s, p, n) :
    if wallCrash(p,n) or selfCrash(s, p) :
        return True
    return False

# 현재 위치에 사과 있는지 확인 및 있으면 먹었다고 간주하고 삭제
def hereApple(p) :
    global Apps
    if p in Apps :
        Apps.remove(p)
        return True
    return False

# 입력값에 따라 방향 전환
def chgDirx(C) :
    global dirx
    if C == "L" :
        dirx = (dirx - 1) % 4
    else :
        dirx = (dirx + 1) % 4

# 방향에 따라 이동 및 확인
def move(d) :
    global r,c
    if d == 0 :
        c += 1
    elif d == 1 :
        r += 1
    elif d == 2 :
        c -= 1
    else : 
        r -= 1
    if chkCrashed(snake, (r,c), N) :
        return False
    snake.append((r,c))
    if not hereApple((r,c)) :
        snake.popleft()
    return True

# 매 초마다 이동 및 확인
while True :
    if not move(dirx) :
        break
    if xcIdx < L and t == int(XCs[xcIdx][0]) :
        chgDirx(XCs[xcIdx][1])
        xcIdx += 1
    t += 1

print(t)




'''
🤔 문제정의를 잘 하자 🤔

입력 : 보드의 크기 N \n 사과의 개수 K \n 사과의 위치 (r,c) \n 뱀 방향 변환 횟수 L \n 뱀의 방향 변환 정보 (int X초, str L or D 왼/오로 90도 방향전환)
출력 : 게임이 몇초 안에 끝나는지

찾아야하는 값 : 뱀이 길어지면서 or 이동하면서 벽 or 자기자신과 부딪히는데 걸리는 시간
알고리즘 : Queue

-----
매 초마다 뱀 머리 위치를 좌표로 기록 -> 사과가 있으면 길이 +1 // 벽이랑 부딛히는지 파악 가능. 자기 몸이랑 부딛히는지는 어떻게 파악?
- 덱으로 초마다 위치 추가 / 삭제 => 몸의 각 위치를 파악하는건 가능함.
- 초마다 어느 방향으로 가는지 확인 필요? 0~3?


예시2)
N = 10
K = 4
App = ((1,2) (1,3) (1,4) (1,5))
L = 4
XCs = ((8,D), (10,D), (11,D), (13,L))

snake = Deque((1,1))

1sec
tail <(1,1) (1,2)> head
사과 있어서 꼬리 안자름
snake.append((1,2))

2sec
tail <(1,1) (1,2) (1,3)> head
사과 있어서 꼬리 안자름
snake.append((1,3))

3sec
tail <(1,1) (1,2) (1,3) (1,4)> head
사과 있어서 꼬리 안자름
snake.append((1,4))

4sec
tail <(1,1) (1,2) (1,3) (1,4) (1,5)> head
사과 있어서 꼬리 안자름
snake.append((1,5))

5sec
tail <(1,2) (1,3) (1,4) (1,5) (1,6)> head
사과없음 꼬리자름
snake.append((1,6))
snake.popleft()

6sec
tail <(1,3) (1,4) (1,5) (1,6) (1,7)> head
사과없음 꼬리자름
snake.append((1,7))
snake.popleft()

7sec
tail <(1,4) (1,5) (1,6) (1,7) (1,8)> head
사과없음 꼬리자름
snake.append((1,8))
snake.popleft()

8sec
tail <(1,5) (1,6) (1,7) (1,8) (1,9)> head
사과없음 꼬리자름
snake.append((1,9))
snake.popleft()

9sec
tail <(1,6) (1,7) (1,8) (1,9) (2,9)> head
사과없음 꼬리자름
snake.append((2,9))
snake.popleft()

...



첫실패 디버깅
https://www.acmicpc.net/board/view/56469

결과, 방향전환 정보로 for문 돌린 후 완료시에 추가로 반복문이 돌지 않아야하는데,
밑에 while문이 바로 돌면서 끝나지 않는 문제.
for ~ else 문으로 해결,,

리팩토링 해보기

-----

'''