from sys import stdin
input = stdin.readline

N = int(input())

k = 0
leng = 3
while leng < N :
    k += 1
    leng = 2 * leng + 3 + k

def moo(k, leng, N) :
    if k == 0:
        if N == 1 :
            return "m"
        else :
            return "o"

    leng = (leng - 3 - k) // 2
    k -= 1

    if N <= leng :
        return moo(k, leng, N)
    
    elif leng < N <= leng + 4 + k :
        if N-leng == 1:
            return "m"
        else :
            return "o"

    else :
        return moo(k, leng, N - leng - 4 - k)

    

print(moo(k, leng, N))









'''

N번째 글자를 구하기 위해 필요한 k 값이 무엇인가를 찾아야 하는 문제 같은데..

N 값을 

또는,, 실제 수열이 어떻게 생겼느냐 하는 수열을 구하는 것과 상관없이, N번째 글자만 알 수 있는 방법이 있을까?


'''






































'''
🤔🤔🤔 문제정의를 잘 하자 🤔🤔🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----



-----


'''