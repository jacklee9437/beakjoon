from collections import deque
from sys import stdin
input = stdin.readline

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수
App = [tuple(map(int,input().split())) for _ in range(K)] # 사과 좌표
L = int(input()) # 방향변환 횟수
XCs = tuple(tuple(input().split()) for _ in range(L)) # 방향변환 정보

def hereApple(pos : tuple, apple : list) -> bool :
    if pos in apple : 
        apple.remove(pos)
        return True
    return False

def chgDirx(C) :
    global dirx
    if C == "D" :
        dirx = (dirx + 1) % 4
    elif C == "L" :
        if dirx > 0 : dirx -= 1
        else : dirx = 3

def crashWall(lim : int, pos : tuple) :
    if pos[0] > lim or pos[1] > lim :
        return True
    if pos[0] < 1 or pos[1] < 1 :
        return True
    return False

def crashSelf(snake : deque, pos: tuple) :
    if pos in list(snake) : return True
    return False

snake = deque()

dirx = 0 # 0 오른쪽 1 아래쪽 2 왼쪽 3 위쪽
r, c = 1, 1
snake.append((r,c))
t = 1

dirxChgIdx = 0

while True :
    if dirx == 0 :
        c += 1
    elif dirx == 1 :
        r += 1
    elif dirx == 2 :
        c -= 1
    else :
        r -= 1
    if crashSelf(snake, (r,c)) or crashWall(N, (r,c)) : break
    snake.append((r,c))
    if not hereApple((r,c), App) :
        snake.popleft()
    if dirxChgIdx < L :
        if int(XCs[dirxChgIdx][0]) == t :
            chgDirx(XCs[dirxChgIdx][1])
            dirxChgIdx += 1
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