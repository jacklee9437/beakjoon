from sys import stdin
input = stdin.readline

def stars(arr) :
    li = []
    star_idx = len(arr)
    for i in range(star_idx*3) :
        if i//star_idx == 1 :
            li.append(arr[i%star_idx] + ' ' * star_idx + arr[i%star_idx])    
        else :
            li.append(arr[i%star_idx] * 3)
    return li


N = int(input())
# K = int(pow(N,1/3)) 이거보다 반복해서 K값 수정해주는게 메모리 덜 잡아먹는듯...
K = 0 
star = ['***','* *','***']

while N != 3:
    N = int(N/3)
    K += 1

for _ in range(K) :
    star = stars(star)

for s in star :
    print(s)

