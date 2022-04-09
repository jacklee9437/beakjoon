from sys import stdin, maxsize
input = stdin.readline

N = int(input())
charVals = tuple(sorted(map(int,input().split())))

ansL = 0
ansR = 0

minVal = maxsize
pL = 0
pR = N-1


while pL < pR :
    tempSum = charVals[pL] + charVals[pR]
    if tempSum == 0 : 
        ansL, ansR = pL, pR
        break
    elif abs(tempSum) < abs(minVal) :
        ansL, ansR = pL, pR
        minVal =  tempSum
    if tempSum < 0 : pL += 1
    else : pR -= 1

print(charVals[ansL], charVals[ansR])
        

    
    




'''
입력 : N , charVals
출력 : 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값 a, b (오름차순). 두 개 이상일 경우는 아무거나 하나 출력

찾아야하는 값 (이분탐색 하려고 하는 결과값 && 선형탐색으로 구할 수 있지만 이분탐색으로 해야 빠른,,,) : 0에 가장 가까운 특성값 (을 만들어내는 두 특성값)

산성 양의 정수
알칼리 음의 정수

특성값이 0에 가까운 용액 만들기


-----

완전탐색을 한다면,,, i와 j 인덱스로 하나하나 뽑아서 모두다 더했을것 같음. 또는 조합 구해서 두개씩 다 더한거의 최소값을 구하거나,,,

음.. 두 원소끼리의 합을 다 구한다음에 그 안에서 0에 가까운 수를 찾는다? - 가능은 하지만 그럼 두 원소가 뭔지는 알수가 없을듯


이분탐색과정에서 중간을 찾았다면, 양 끝으로 칮아본다?
양끝에서 합이 -면 L포인터를 +쪽으로, +면 R포인터를 -쪽으로



-----

'''