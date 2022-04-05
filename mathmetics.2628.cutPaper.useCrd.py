import time
from sys import stdin
input = stdin.readline

# 확인 함수 (필요시)
def max_len(l,arr) :
    pos = [0] * l
    pos[l-1] = 1
    max = 0
    pres_p = 0
    prev_p = 0
    for i in arr :
        pos[i-1] = 1
    for j in range(l) :
        if pos[j] == 1 :
            prev_p = pres_p
            pres_p = j+1

            if (max < pres_p - prev_p )  :
                max = pres_p - prev_p
    return max
            


# 풀이 함수
def solve(w,h,cuts) :
    x_max = w
    y_max = h
    x_cuts = []
    y_cuts = []
    for cut in cuts :
        cor, s = map(int,cut.split())
        if cor == 0 :
            y_cuts.append(s)
        elif cor == 1 :
            x_cuts.append(s)
    x_max = max_len(w,x_cuts)
    y_max = max_len(h,y_cuts)

    print(x_max * y_max)
    




if __name__ == "__main__" :

    # 입력
    w,h = map(int,input().split())
    n = int(input())
    cuts = [input() for _ in range(n)]



    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    solve(w,h,cuts)



    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {end - start:.5f} sec")

