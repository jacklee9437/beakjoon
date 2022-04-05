from itertools import permutations
import time
from sys import stdin
input = stdin.readline

'''
-------- Concept --------



결과값을 리스트에 집어넣고 마지막에 최대/최소값 출력하기

'''


# 필요한 함수
def opers_from_cnt(opers_cnt) :
    opers = []
    for i,v in enumerate(opers_cnt) :
        [opers.append(i) for _ in range(v)]
    return opers

def cal_of(l, i, opers) -> int :
    if i == n-1 : result_list.append(l)
    else : 
        if opers[i] == 0 :
            cal_of(l + a[i+1], i+1, opers)
        elif opers[i] == 1 :
            cal_of(l - a[i+1], i+1, opers)
        elif opers[i] == 2 :
            cal_of(l * a[i+1], i+1, opers)
        else :
            cal_of(l//a[i+1] if l > 0 else -((-l)//a[i+1]),i+1,opers)



if __name__ == "__main__":

    # 입력
    n = int(input())
    a = list(map(int,input().split()))
    opers_cnt = list(map(int,input().split()))
    
    # 풀이시작전 기록
    # start = time.time()
    

    # 문제 풀이
    opers = opers_from_cnt(opers_cnt)
    opers_perm = list(set(permutations(opers)))

    result_list = []

    for o in opers_perm :
        cal_of(a[0], 0, o)
        
    
    print(max(result_list))
    print(min(result_list))
    

    
    

    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {(end - start)*1000:.5f} ms")
