# import time
from sys import stdin
input = stdin.readline

# 확인 함수 (필요시)
def hanoi_cnt(n) :
    if n == 1 : return 1
    return 2 * hanoi_cnt(n-1) + 1

def hanoi_trace(a,b,n) :
    if n > 1 :
        hanoi_trace(a, 6-a-b, n-1)
        li.append(str(a) + ' ' + str(b))
        hanoi_trace(6-a-b,b,n-1)
    else :
        li.append(str(a) + ' ' + str(b))

    
        

# 풀이 함수
def solve(n) :
    if (n > 20) :
        print(hanoi_cnt(n))
    else :
        hanoi_trace(1,3,n)
        print(len(li))
        for i in li :
            print(i)
    




if __name__ == "__main__" :

    # 입력
    n = int(input())
    li = []


    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    solve(n)
    

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {end - start:.5f} sec")

