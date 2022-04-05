import time
from sys import stdin
input = stdin.readline

# 확인 함수 (필요시)
# def 


# 풀이 함수
def solve(n) :
    return n * solve(n-1) if (n > 0) else 1
    
    




if __name__ == "__main__" :

    # 입력
    n = int(input())



    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    print(solve(n))



    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {end - start:.5f} sec")

