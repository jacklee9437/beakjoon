import time
from sys import stdin
input = stdin.readline

# 확인 함수 (필요시)
# def 


# 풀이 함수
def solve(n,i) :
    if (n > 0) : 
        print('____' * i + '"재귀함수가 뭔가요?"')
        print('____' * i + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____' * i + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('____' * i + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        solve(n-1,i+1)
        print('____' * i + '라고 답변하였지.')
    else :
        print('____' * i + '"재귀함수가 뭔가요?"')
        print('____' * i + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print('____' * i + '라고 답변하였지.')
    
    




if __name__ == "__main__" :

    # 입력
    n = int(input())



    # 풀이시작전 기록
    # start = time.time()

    # 풀이 함수 실행
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    solve(n,0)



    # 풀이 완료 기록 및 출력
    # end = time.time()
    # print(f"소요시간 : {end - start:.5f} sec")

