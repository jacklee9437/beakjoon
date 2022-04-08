#이진검색

# while문 활용
def binary_search(arr, key) :
    left = 0
    right = len(arr) - 1
    

    while True :
        chk_idx = (left + right) // 2
        if arr[chk_idx] == key :
            return chk_idx
        if arr[chk_idx] > key :
            right = chk_idx-1
        else :
            left = chk_idx+1
        if left > right : return -1
        
        
# 재귀 적용
def binary_search_recul(arr, key, left, right) :
    chk_idx = (left + right) // 2
    if arr[chk_idx] == key : return chk_idx
    if arr[chk_idx] > key :
        if left > chk_idx-1 : return -1
        return binary_search_recul(arr, key, left, chk_idx-1)
    else :
        if chk_idx+1 > right : return -1
        return binary_search_recul(arr, key, chk_idx+1, right)



a = [1, 3, 4, 5, 6, 8, 12]

print(binary_search(a,3))
print(binary_search_recul(a, 12, 0, len(a)-1))