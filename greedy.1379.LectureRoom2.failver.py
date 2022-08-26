'''
시간초과 발생한 버전.
회의실 배정 문제와 같이, 회의실을 고정해놓고 최대한 배정해준 후 회의실을 바꾸는 컨셉.
강의 개수가 너무 커서 반복문 돌리면 메모리초과,시간초과 당연히 발생함.
따라서 여러번 돌리지 않고 한번에 해결할 방법을 찾아야함
'''


from sys import stdin
input = stdin.readline

N = int(input())
lects = [list(map(int, input().split())) for _ in range(N)]
lects.sort(key=lambda x: (x[1],x[2]))

print(*lects, sep='\n')

room = 1
assigned = [0] * (N+1)
while lects:

    lect = lects[0]
    lects.remove(lect)
    end = lect[2]
    assigned[lect[0]] = room

    for l in lects:
        no, st, et = l
        if st >= end:
            assigned[no] = room
            lects.remove(l)
            end = et

    room += 1

# print(room-1)
# print(*assigned[1:], sep='\n')
