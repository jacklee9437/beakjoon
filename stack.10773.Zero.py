from sys import stdin, maxsize
input = stdin.readline

class Stack :
    def __init__(self, capacity) :
        self.capacity = capacity
        self.stk = [0] * capacity
        self.ptr = 0
    
    def push(self, val) :
        self.stk[self.ptr] = val
        self.ptr += 1

    def pop(self) :
        if self.ptr > 0 :
            self.ptr -= 1
        else : 
            pass

    def size(self) :
        print(self.ptr)

    def empty(self) :
        print(0 if self.ptr>0 else 1)

    def top(self) :
        print(self.stk[self.ptr-1] if self.ptr>0 else -1)

    def sum(self) :
        return sum(self.stk[:self.ptr])

K = int(input())
stk = Stack(K)

for _ in range(K) :
    inputNum = int(input())

    if inputNum == 0 : stk.pop()
    else :
        stk.push(inputNum)

print(stk.sum())




    


'''
🤔 문제정의를 잘 하자 🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----


-----

'''