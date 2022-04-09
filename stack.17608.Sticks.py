from sys import stdin, maxsize
input = stdin.readline

class Stack :
    def __init__(self, capacity) :
        self.capacity = capacity
        self.stk = [0] * capacity
        self.ptr = 0
    
    def push(self, val=1) :
        self.stk[self.ptr] = val
        self.ptr += 1

    def pop(self) :
        if self.ptr > 0 :
            self.ptr -= 1
            return self.stk[self.ptr]

    def empty(self) :
        return True if self.ptr==0 else False


N = int(input())
stk = Stack(N)

for _ in range(N) :
    stk.push(int(input()))

right = stk.pop()
cnt = 1
while not stk.empty() :
    temp = stk.pop()
    if temp > right : 
        right = temp # 처음 맨 오른쪽꺼보다 크더라도 맨 오른쪽꺼보다 크지만 현재보다 오른쪽에 있는 막대기에 의해 가려질 수 있으므로 right를 갈아끼워줄 필요가 있음.
        cnt += 1

print(cnt)

    


'''
🤔 문제정의를 잘 하자 🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----


-----

'''