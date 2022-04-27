from sys import stdin, maxsize
input = stdin.readline

N, K = map(int,input().split())
things = list(map(int,input().split()))

class multitab :
    def __init__(self, size) :
        self.size = size
        self.pluged = set()
        self.cnt = 0

    def plug(self, cord) :
        if cord in self.pluged :
            return True
        if self.isfull() :
            return False
        self.pluged.add(cord)
        self.cnt += 1
        return True
    
    def unplug(self, cord) :
        try :
            self.pluged.remove(cord)
            self.cnt -= 1
            return True
        except :
            return False

    def isfull(self) :
        return True if self.size == self.cnt else False

mtt = multitab(N)
cnt = 0
for idx, thing in enumerate(things) :
    if mtt.plug(thing) :
        continue
    
    temp = (0,0)
    for p in mtt.pluged :
        if p not in things[idx:] :
            temp = (p,)
            break
        i = things[idx:].index(p)
        temp = (p, i) if temp[1] < i else temp
    mtt.unplug(temp[0])
    mtt.plug(thing)
    cnt += 1

print(cnt)
