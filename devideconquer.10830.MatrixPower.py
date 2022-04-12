from sys import stdin
input = stdin.readline

N, B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

def power(A,B,n) :
    rst = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            for k in range(n) :
                rst[i][j] += A[i][k] * B[k][j]
                # print("%d += A[%d][%d] * B[%d][%d]"%(sum,i,k,k,j))
            rst[i][j] %= 1000
    return rst

def powMtrx(A,b,n) :
    if b == 1 :
        for i in range(n) : # 1인 경우에도 %1000은 해줘야함...
            for j in range(n) :
                A[i][j] %= 1000
        return A
    elif b == 2 :
        return power(A,A,n)
    elif b % 2 == 0 :
        return powMtrx(powMtrx(A,b//2,n),2,n)
    else :
        return power(powMtrx(powMtrx(A,b//2,n),2,n),A,n)
        
ans = powMtrx(A, B, N)
for i in range(N) :
    # for j in range(N) : %계산을 중간에 많이 안하려고 마지막에 넣었지만, 결국 for문 한번 더돌리면서 오히려 시간 잡아먹음. 그냥 앞에 넣는게 나은듯.
        # ans[i][j] %= 1000
    print(' '.join(map(str,ans[i])))




'''
🤔 문제정의를 잘 하자 🤔

입력 : 행렬의 크기 N 제곱 B , 행렬 A
출력 : A의 B제곱 %1000

찾아야하는 값 : 
알고리즘 : 분할정복

-----


-----

'''