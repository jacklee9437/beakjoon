from sys import stdin
input = stdin.readline

class Stack :
    def __init__(self, capacity) :
        self.stk = [0] * capacity
        self.ptr = 0
    
    def push(self, val) :
        self.stk[self.ptr] = val
        self.ptr += 1

    def pop(self, val=1) :
        if self.ptr > 0 :
            self.ptr -= val

    def top(self) :
        return self.stk[self.ptr-1]

    def empty(self) :
        return True if self.ptr<=0 else False


N, K = map(int,input().split())
num = input().strip()

stk = Stack(N)

for char in num :
    while not stk.empty() :
        if stk.top() < char and K != 0 :
            stk.pop()
            K -= 1
        else : 
            break
    stk.push(char)

# for _ in range(K) : 팝을 해서 지워주는 방법도 있지만 시간 소모. 그냥 인덱스에서 빼주기
#     stk.pop()

for char in stk.stk[:stk.ptr-K] :
    print(char, end='')









'''
🤔 문제정의를 잘 하자 🤔

입력 : 자리수 N, 뺄개수 K, 숫자 num
출력 : 얻을 수 있는 가장 큰 수

찾아야하는 값 : 얻을 수 있는 수 중의 가장 큰 수
알고리즘 : 완전탐색? 이분탐색? 스택?

-----
완전탐색?
- 자리수 N에서 K를 빼면 결과로 얻을 수 있는 숫자의 자리수를 알 수 있으므로, num에서 그 자리수만큼 combination을 구한다음 원 순서에 맞게 재구성하고 최대값을 구하는 방법 - 원래 위치대로 바꿔줘야하고 모든 경우의 수를 따지면 너무 오래걸림
- 글자에서 처음부터 가면서 가장 큰거, 그 다음 큰거, 그다음 큰거 구하면서 K개 버려지고나면 나머지는 그대로 출력하는 방법
    - 주의해야할 점 : 숫자의 순서가 바뀌면 안됨! -> 오히려 힌트임. 작은 숫자가 앞에 있는게 당연히 안좋기때문에 작은 값보다 큰값을 발견하면 바로 버릴 수 있음! 뒤에서 가장 큰 값이 나오더라도 어차피 앞으로 오지는 못함!
    - 꼭 스택이어야 하나? 그냥 변수에 저장해도 되는거 아닌가? -> 그러면 924 같은 경우에 9보다 작아서 2,4를 아예 저장을 못함. 스택으로 해서 작아도 일단 저장한다음 후에 큰게 있으면 빠지는 식으로 해야할듯.

- 실패원인
K가 남는경우를 고려하지 못했음.
예를들어, 비교대상이 항상 이전값보다 작다면 계속 push만 됨. 즉 더 빠지지 않음...
- 해결방법
1. 일단 한번 한게 최대로 만들기는 했지만 추가로 더 빼줄 수 있는 상태인거니까 for문 말고 while로 바꾸고 K가 0이 될때까지 루프 반복되도록?  => 안됨. 구현한 방법 자체가 순서를 유지하면서 큰거부터 나열되도록 만든거,,
2. 다 끝나고나서 맨 마지막에 K만큼을 빼주기 or 중간에서 K가 0이 안된경우에 고려해줄 수 있는 부분?

- 돌아보기
스택/큐 는 정렬이나 데이터를 찾기위한 자료구조라기보다는 문제를 해결하기 위해 중간에서 사용되는 임시 저장소라고 봐야함.
따라서 일단 완전탐색 등의 방법으로 문제를 접근하고, 그 과정에서 LIFO/FIFO 중 사용할 수 있는 방법이 있을지 고민해봐야함.
-----

'''