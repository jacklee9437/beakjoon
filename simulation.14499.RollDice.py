from sys import stdin
input = stdin.readline

class Dice :
    def __init__(self, map, cord) :
        self.map = map[:]
        self.dice = [0] * 6
        self.cord = cord[:]
    def roll(self, d) :
        if d == 1 :
            tmp = self.dice[0]
            self.dice[0] = self.dice[3]
            self.dice[3] = self.dice[5]
            self.dice[5] = self.dice[1]
            self.dice[1] = tmp
        elif d == 2 :
            tmp = self.dice[0]
            self.dice[0] = self.dice[1]
            self.dice[1] = self.dice[5]
            self.dice[5] = self.dice[3]
            self.dice[3] = tmp
        elif d == 3 :
            tmp = self.dice[0]
            self.dice[0] = self.dice[2]
            self.dice[2] = self.dice[5]
            self.dice[5] = self.dice[4]
            self.dice[4] = tmp
        else :
            tmp = self.dice[0]
            self.dice[0] = self.dice[4]
            self.dice[4] = self.dice[5]
            self.dice[5] = self.dice[2]
            self.dice[2] = tmp
        r, c = self.cord
        bottom = self.map[r][c]
        if bottom == 0 :
            self.map[r][c] = self.dice[0]
        else :
            self.dice[0] = self.map[r][c]
            self.map[r][c] = 0
        print(self.dice[5])
    def tryRoll(self, d) :
        if d == 1 :
            if self.cord[1] == len(self.map[0]) - 1 :
                return
            self.cord[1] += 1
        elif d == 2 :
            if self.cord[1] == 0 :
                return
            self.cord[1] -= 1
        elif d == 3 :
            if self.cord[0] == 0 :
                return
            self.cord[0] -= 1
        else :
            if self.cord[0] == len(self.map) - 1 :
                return
            self.cord[0] += 1
        self.roll(d)

# 0하 1왼 2앞 3오 4뒤 5상

N, M, x, y, K = map(int, input().split())
diceMap = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

dice = Dice(diceMap, [x,y])
for cmd in command :
    dice.tryRoll(cmd)