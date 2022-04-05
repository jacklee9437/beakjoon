import sys
from typing import Sequence

def cnt_num_of(multi):
    seq_multi = list(map(int,str(multi)))
    cnt = [0] * 10

    for i in seq_multi :
        cnt[i] += 1

    return cnt




if __name__ == "__main__" :
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())

    multi = a * b * c
    
    cnt = cnt_num_of(multi)

    for j in cnt :
        print(j)