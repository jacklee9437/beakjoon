from sys import stdin
input = stdin.readline

N = int(input())
paper = tuple(tuple(map(int,input().split())) for _ in range(N))

whiteCnt = 0
blueCnt = 0

def cut_paper(arr, n, p : tuple = (0, 0)) :
    global whiteCnt, blueCnt
    color = arr[p[0]][p[1]]
    isBraked = False
    for i in range(p[0],p[0]+n) :
        for j in range(p[1],p[1]+n) :
            if arr[i][j] != color :
                isBraked = True
                break
        else : continue
        break
    else :
        if color == 1 :
            blueCnt += 1
        else :
            whiteCnt += 1
    if isBraked :
        cut_paper(arr, n//2, (p[0],p[1]))
        cut_paper(arr, n//2, (p[0],p[1]+n//2))
        cut_paper(arr, n//2, (p[0]+n//2,p[1]))
        cut_paper(arr, n//2, (p[0]+n//2,p[1]+n//2))

cut_paper(paper, N)
print(whiteCnt)
print(blueCnt)


'''
🤔 문제정의를 잘 하자 🤔

입력 : 전체 종이 한변의 길이 N, 색종이의 정사각형 색들 정보 (NbyN) (흰색 0 파란색 1)
출력 : 하얀색 종이 개수 whiteCnt \n 파란색 종이 개수 blueCnt

찾아야하는 값 : 흰/파란 색 종이 개수
알고리즘 : 분할정복법,,, -> 재귀? 또는 반복문?

-----
N이 1이 될때까지 재귀적으로 들어가서 all로 다 1이거나 다 0인지 찾고 아니면 다시 찢어서 재귀로 들어가고, 맞으면 cnt 올리도록.

열마다 들어가면서 확인 필요.
all 이 True여서 전부 1이면 whiteCnt + 1
any로 True 나오면 1섞인거니까 분할
any가 False 나오면 0만 있으니까 blueCnt + 1

재귀 돌릴때 arr, N, 사분면만 전달시에 재귀호출해서 다음단계 진행시 배열을 어디서부터 끊어야할지가 어려움. 추가 인자 전달 필요.
사분면에 따라 실제 위치 (하나만) 전달해주기.

-----

'''