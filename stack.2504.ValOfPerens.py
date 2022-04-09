from sys import stdin
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
        # if self.ptr > 0 :
        self.ptr -= 1
        return self.stk[self.ptr] if self.ptr >= 0 else -1

    def empty(self) :
        return True if self.ptr==0 else False



stk = Stack(30)
perens = input().strip()
cal = [0] * 16

for peren in perens :
    if peren == "(" :
        stk.push(2)
        continue
    elif peren == "[" :
        stk.push(3)
        continue
    elif peren == ")" :
        peren = 2
    else : 
        peren = 3
    
    temp = stk.pop()
    tempPtr = stk.ptr + 1

    if temp == -1 : 
        print(0)
        break
    if peren != temp :
        print(0)
        break
    if cal[tempPtr] == 0 : cal[stk.ptr] += temp
    else : cal[stk.ptr] += cal[tempPtr] * temp
    cal[tempPtr] = 0
else : 
    if stk.empty() :
        print(cal[0])
    else :
        print(0)



    

    


'''
🤔 문제정의를 잘 하자 🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----


-----

'''