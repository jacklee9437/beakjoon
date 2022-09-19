from sys import stdin
input = stdin.readline

Towns, Capacity = map(int, input().split())
M = int(input())
Orders = [list(map(int, input().split())) for _ in range(M)]

Orders.sort(key=lambda x: (x[1], x[0]))

loadAmount = [0] * (Towns+1)
totalDelivery = 0

for order in Orders :
    sender, receiver, boxes = order
    limit = Capacity - max(loadAmount[sender: receiver])
    if limit > 0 :
        for i in range(sender, receiver) :
            box = min(limit, boxes)
            loadAmount[i] += box
        totalDelivery += box 

print(totalDelivery)