from math import ceil
import time
from sys import stdin
input = stdin.readline

# 확인 함수 (필요시)
def z_recul(n,r,c) :
    if (n==1) :
        return z_p[r][c]
    else :
        z = pow(2, n-1)
        z_max = pow(z, 2)
        z_x = ceil((r+1)/z)-1
        z_y = ceil((c+1)/z)-1

        # if (z_x == 0) :
        #     if (z_y == 0) : 
        #         return 0 * z_max + z_recul(n-1,r%z,c%z)
        #     else :
        #         return 1 * z_max + z_recul(n-1,r%z,c%z)
        # else :
        #     if (z_y == 0) :
        #         return 2 * z_max + z_recul(n-1,r%z,c%z)
        #     else :
        #         return 3 * z_max + z_recul(n-1,r%z,c%z)
        # 왜 안되는지 잘 모르겠네...


        new_r = r%z
        new_c = r%z
        return z_p[z_x][z_y] * z_max + z_recul(n-1,new_r,new_c)

# 풀이 함수
def solve(n,r,c) :
    print( z_recul(n,r,c) )



'''
r행 c열이 어느 위치에?

n이 1이라면? -> 2 by 2
1번 방문이 끝 (2^0 x 2^0) -> 그 안에서 몇번째인지 찾으면 됨

n이 2라면? -> 4 by 4
최소 1번 최대 4번 방문해야함 (2^1 x 2^1) -> 행 열에 따라서 몇번 방문하는지, 그리고 마지막 방문 몇번째인지

n이 3이라면? -> 8 by 8
최소 1번 최대 16번 방문해야함 (2^2 x 2^2) -> 동일한 방법,,,

=> 행 열의 위치로 어디 위치까지 방문해야하는지 보고, 재귀적으로 방문하면 될 것 같은데...


n이 3, r이 7, c가 7이면,,,

    Z(3,7,7)
    모든 Z에 대해서,,.
    z(3) = 2^(3-1)
    z_x, z_y = ceil(7/z), ceil(7/z) : 2,2
    new_r, new_c = 7%z, 7%z : 3,3
    1,1 -> 1 = Z_max(2)가 0번 --- 여기서 Z_max는 n=2인 배열(2^2 x 2^2)의 최대원소수 (16)
    2,1 -> 2 = Z_max(2)가 1번
    1,2 -> 3 = Z_max(2)가 2번
    2,2 -> 4 = Z_max(2)가 3번 -> 더해줌.
    추가로 Z(2)를 실행하면서, r과 c를 넘겨줌 -> Z(2,3,3)?

    Z(2,3,3)
    z(2) = 2^(2-1)
    z_x, z_y = ceil(3/z), ceil(3/z) : 2, 2
    new_r, new_c = 3%z, 3%z : 1, 1
    Z_max(1)가 3번 + Z(1,1,1)

Z(3,7,7) =  + Z(2,3,3)
'''







if __name__ == "__main__" :

    # 입력
    n, r, c = map(int,input().split())
    z_p = [[0,1],[2,3]]

    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    # for n in range(1,16) :
    #     for r in range(pow(2,n)) :
    #         for c in range(pow(2,n)) :
    solve(n, r, c)
    

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")
