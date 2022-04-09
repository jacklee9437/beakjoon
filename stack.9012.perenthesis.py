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
        # if self.ptr > 0 :
        self.ptr -= 1

    def empty(self) :
        return True if self.ptr==0 else False

T = int(input())
for _ in range(T) :
    stk = Stack(50)
    case = input().strip()
    for paren in case :
        if paren == "(" :
            stk.push()
        else :
            stk.pop()
            if stk.ptr < 0:
                print("NO")
                break
    else :
        if stk.empty() :
            print("YES")
        else :
            print("NO")


    


'''
🤔 문제정의를 잘 하자 🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----


-----

'''