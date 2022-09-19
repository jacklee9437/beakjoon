class Heap :
    def __init__(self) :
        self.que = [0]

    def isEmpty(self) :
        return not (len(self.que)-1)

    def push(self, val) :
        self.que.append(val)
        
        idx = len(self.que)-1
        pidx = idx//2

        while pidx >= 1 :
            if self.que[pidx] < self.que[idx] :
                tmp = self.que[pidx]
                self.que[pidx] = self.que[idx]
                self.que[idx] = tmp
                idx = pidx
                pidx //= 2
            else :
                break
        
    def pop(self) :
        if self.isEmpty() :
            return 0
        ret = self.que[1]
        self.que[1] = self.que[-1]
        self.que.pop()
        pidx = 1
        while (pidx << 1) < len(self.que) :
            if pidx*2+1 < len(self.que) :
                if self.que[pidx] > self.que[pidx*2] and self.que[pidx] > self.que[pidx*2+1] :
                    break
                elif self.que[pidx*2+1] < self.que[pidx*2] :
                    tmp = self.que[pidx]
                    self.que[pidx] = self.que[pidx*2]
                    self.que[pidx*2] = tmp
                    pidx = pidx*2
                else :
                    tmp = self.que[pidx]
                    self.que[pidx] = self.que[pidx*2+1]
                    self.que[pidx*2+1] = tmp
                    pidx = pidx*2+1
            else :
                if self.que[pidx] > self.que[pidx*2] :
                    break
                else :
                    tmp = self.que[pidx]
                    self.que[pidx] = self.que[pidx*2]
                    self.que[pidx*2] = tmp
                    pidx = pidx*2
        return ret
    
heap = Heap()
heap.push(1)
print(heap.que)
heap.push(7)
print(heap.que)
heap.push(2)
heap.push(3)
heap.push(2)
print(heap.que)
heap.push(100)
print(heap.que)
heap.push(73)
print(heap.que)
while not heap.isEmpty() :
    print(heap.pop())

