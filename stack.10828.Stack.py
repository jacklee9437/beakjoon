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
            print(self.stk[self.ptr])
        else : 
            print(-1)

    def size(self) :
        print(self.ptr)

    def empty(self) :
        print(0 if self.ptr>0 else 1)

    def top(self) :
        print(self.stk[self.ptr-1] if self.ptr>0 else -1)

N = int(input())
stk = Stack(N)
for _ in range(N) :
    cmd = input().split()

    if cmd[0] == "push" :
        stk.push(int(cmd[1]))
    elif cmd[0] == "top" :
        stk.top()
    elif cmd[0] == "size" :
        stk.size()
    elif cmd[0] == "empty" :
        stk.empty()
    elif cmd[0] == "pop" : 
        stk.pop()


    


'''
🤔 문제정의를 잘 하자 🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----


-----

'''