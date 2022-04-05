import sys
from typing import Sequence

def mean_of(arr : Sequence, n : int) -> float :
    sum = 0
    for i in arr :
        sum += i
    mean = sum/n
    return mean

def per_over_mean_of(arr : Sequence, n : int, mean : float) -> float :
    cnt = 0
    for i in arr :
        if (i > mean) :
            cnt += 1

    per_over_mean = format(cnt/n * 100, ".3f")
    return per_over_mean


if __name__ == "__main__" :
    c = int(sys.stdin.readline())
    cases = [sys.stdin.readline().strip() for i in range(c)]

    for i in cases :
        case = list(map(int,i.split()))
        n = case[0]
        case = case[1:]

        mean = mean_of(case, n)
        per_over_mean = per_over_mean_of(case, n , mean)
        print(per_over_mean[:6] + '%')



