import time
from sys import stdin
input = stdin.readline

# 확인 함수 (필요시)
def n_queen(x) :
    if ( n > x ) :
        for i in range(n) :
            if chk_line[i] or chk_ru[n + x - i - 1] or chk_rd[(2 * n - 2) - x - i] : continue
            else :
                xy_map[x] = i
                chk_line[i] = chk_ru[n + x - i - 1] = chk_rd[(2 * n - 2) - x - i] = True
                n_queen(x+1)
                chk_line[i] = chk_ru[n + x - i - 1] = chk_rd[(2 * n - 2) - x - i] = False
    else :
        cnt[0] += 1

'''
1행 1열 = ru 8 rd 15
1행 2열 = ru 9 rd 14
1행 3열 = ru 10 rd 13
...
i행 x+1열 = ru ? + x+1 rd ?? - x+1

1행 1열 = ru 8 rd 15
2행 1열 = ru 7 rd 14

i행 x+1열 = ru ? - i rd ?? - i

=> i행 x+1열 = ru : 8 + x -i rd : 17 - x - i
'''

# 풀이 함수
def solve(n) :
    n_queen(0)
    print(cnt[0])
    




if __name__ == "__main__" :

    # 입력
    n = int(input())
    xy_map = [0] * n #idx가 x, value가 y
    chk_line = [False] * n
    chk_ru = [False] * (2 * n - 1)
    chk_rd = [False] * (2 * n - 1)
    cnt = [0]

    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    solve(n)

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")

