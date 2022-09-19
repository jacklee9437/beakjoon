from sys import maxsize, stdin
input = stdin.readline

def dist_bt_dots(dot1, dot2) :
    a = abs(dot1[0] - dot2[0])
    b = abs(dot1[1] - dot2[1])
    return a**2 + b**2


n = int(input())
dots = sorted([tuple(map(int,input().split())) for _ in range(n)])

mindist = maxsize

def get_min_dist(start, end, arr=dots) :
    if start == end :
        return maxsize
    
    if end - start == 1 :
        return dist_bt_dots(arr[start],arr[end])
    
    mid = (end+start) // 2
    mindist = min(get_min_dist(start, mid),get_min_dist(mid,end))

    templist = []
    
    for i in range(start,end+1) :
        if abs(arr[mid][0] - arr[i][0])**2 < mindist :
            templist.append(arr[i])

    templist.sort(key= lambda x: x[1])
    templen = len(templist)
    for i in range(templen - 1) :
        for j in range(i+1, templen) :
            if abs(templist[i][1] - templist[j][1])**2 < mindist :
                mindist = min(mindist, dist_bt_dots(templist[i],templist[j]))
            else :
                break
    return mindist

mindist = get_min_dist(0,n-1)
print(mindist)





'''
🤔🤔🤔 문제정의를 잘 하자 🤔🤔🤔

입력 : 자연수 n, 각 점의 x,y좌표
출력 : 가장 가까운 두 점의 거리의 제곱 (가로세로 제곱의 합)

찾아야하는 값 : 각 점에서 다른 점들 사이의 x,y 간격이 짧은 것들. 그 중에서 제일 짧은거?
알고리즘 : 기하학 (a2 + b2 = c2 인듯), 분할정복, 스위핑(하나씩 스캔?)

-----
그냥 단순하게 정말 모든 계산을 다한다고 한다면,
n개 좌표에서 2개씩 뽑는 조합을 구하고, 그 조합에서 각각 거리 구하면서 min값 갱신해서 출력하면 됨.
하지만 시간/공간 복잡도에서 안좋은것.

작은 수준으로 분할할 수 있을까?

일단 각 점들을 다 확인하긴 해야함. 하지만 이미 확인한 부분은 확인하지 않아야함.

2차원을 1차원적으로 : x 축만 먼저 생각
스위핑 하기 위해서 주어진 데이터를 먼저 쏘팅
맨 왼쪽 점부터 확인. x축 방향 간격 확인 후 y축 방향 확인. 
- 그냥 간격들이 작은것들로 저장해두고 나중에 제곱합을 구한다? 아니면 제곱합을 계속 구하면서 최소인지 판단한다? 전자는 계속 비교해야해서 오히려 느리지 않을까? 그냥 점마다 제곱합 구한 다음에 갱신하는 방법?
확인한 점은 추가 확인 대상에서 제외.
=> 가능은 할듯하나 조합 방법만큼이나 비효율적이므로 시간초과 나올듯. 일단 해보자.

좀더 분할정복답게 할 수 있는 방법 있을까? 수 자체가 너무 큰데...
애초에 x 거리가 멀면 너무 멀어지지않을까 싶긴 함. -> 최소/최대 기준으로 사분면 나누듯이 나눠서 각각 확인하고 그중 최소를 구하는 방식이라면? - 경계에 있는 점들 사이에 오히려 가까운 점이 있을 수 있다는 점이 문제...

나눠서 하는건 맞다 싶은데, 경계에 있는 애들은 어떻게 처리해야할지 모르겠음...
답보고 공부 ㅠ
https://my-coding-notes.tistory.com/103

반복연산을 줄이기 위해서 나누는것까진 생각 잘 했음.
한번에 계산해야된다고 생각하니 경계에 있는, 계산이 한번씩만 되고 넘어가는 애들은 어떡하지 어려웠음.
최초 분할해서 계산한 최소거리는 추가로 확인할때 계산을 할것인가 말것인가에 대한 기준이 됨.

- x축 정렬 후 절반 나눠서 절반씩 쭉쭉 확인함.
- 최소거리가 정해지고 나면, x의 중간으로부터 점들에 대해서 최소거리보다 짧은 애들에 한해서 추가 확인할 수 있도록 리스트에 담아줌 -> 추가 연산이 들어가는데, x축 방향으로만 계산하고있어서 모든 점에대해 거리계산하는 것보다 효율적임.
- 담아준 리스트를 y축 방향 기준으로 정렬하고 y축 방향으로 다시한번 확인함. 최소거리 이상인건 버리고, 그 이하인애들에 한해서 거리를 구하고 min 값 갱신해줌.
- 재귀적 호출






-----


'''