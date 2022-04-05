import time
from sys import stdin
input = stdin.readline

def is_hansu(n) :
    result = True
    e = list(map(int,str(n)))
    
    if ( len(e) > 2 ) :
        interval = e[0] - e[1]
        for i in range(1, len(e) -1):
            if ((e[i] - e[i+1]) != interval) : result = False

    return result


# 풀이 함수
def solve(case) :
    cnt = 0
    for i in range(1,case+1) :
        if (is_hansu(i)) : cnt += 1
    print(cnt)




if __name__ == "__main__" :

    # 입력
    n = int(input())



    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    solve(n)



    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {end - start:.5f} sec")

