from sys import stdin, maxsize
input = stdin.readline

# N = int(input())
# paper = tuple(tuple(map(int,input().split())) for _ in range(N))

# whiteCnt = 0
# blueCnt = 0

def cut_paper(arr, n, quadrant=0) :
    for i in range(n) :
        if all(arr[i]) 


arr= [1,1,1]

print(arr)
print(not arr)

print(arr - )



all()
'''
🤔 문제정의를 잘 하자 🤔

입력 : 전체 종이 한변의 길이 N, 색종이의 정사각형 색들 정보 (NbyN) (흰색 0 파란색 1)
출력 : 하얀색 종이 개수 whiteCnt \n 파란색 종이 개수 blueCnt

찾아야하는 값 : 흰/파란 색 종이 개수
알고리즘 : 분할정복법,,, -> 재귀? 또는 반복문?

-----
N이 1이 될때까지 재귀적으로 들어가서 all로 다 1이거나 다 0인지 찾고 아니면 다시 찢어서 재귀로 들어가고, 맞으면 cnt 올리도록.

all 이 True여서 전부 1이면 whiteCnt + 1
any로 True 나오면 1섞인거니까 분할
any가 False 나오면 0만 있으니까 blueCnt + 1

-----

'''