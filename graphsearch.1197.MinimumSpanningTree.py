from sys import stdin, setrecursionlimit
input = stdin.readline

# 입력
V, E = map(int,input().split())
edges = []
for _ in range(E) :
    A,B,C = map(int,input().split())
    edges.append((C,(A,B)))

# 가중치 기준 오름차순 정렬
edges.sort()

# 예제 입력
# V, E = (9, 14)
# edges =[(4,(1,2)), (8,(2,3)), (7,(3,4)), (9,(4,5)), (10,(5,6)), (2,(6,7)), (1,(7,8)), (11,(2,8)), (7,(8,9)), (6,(7,9)), (2,(3,9)), (4,(3,6)), (14,(4,6))]
# edges.sort()

rst = 0

# 대표 vertex (부모) 저장
parents = [i for i in range(V+1)]

# 대표 vertex 반환 / 평탄화 함수
def find(n) :
    # 부모를 찾고 자기 자신이면 바로 반환, 자기 자신이 아니면 재귀적 호출 후 대표점 반환
    if parents[n] != n :
        parents[n] = find(parents[n])
        return parents[n]
    return parents[n]

# 합치는 함수
def union(a,b) :
    pa = find(a)
    pb = find(b)
    # print("a : %d, b : %d, pa : %d, pb : %d" %(a,b,pa,pb))
    # a와 b의 대표점이 다르면 연결안된 그래프이므로 연결, 같으면 합치지 않음.
    if pa != pb :
        # 실제 가리키는게 중요한게 아니라 연결이 되는게 중요하기 때문에 현재 것들끼리 연결일 필요가 없음. 부모끼리 한 방향으로 연결만 되면 됨.
        parents[pa] = pb
        # print("parents[%d] = %d" %(a,b))
        # print(parents)
        return True
    return False

# print(parents)
for edge, vs in edges :
    a, b = vs
    if union(a,b) :
        rst += edge
# print(parents)
    
print(rst)