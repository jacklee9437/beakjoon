import sys


def max_of(array):
    maximum = array[0]
    idx = 1

    for i in range(1, 9):
        if (maximum < array[i]):
            maximum = array[i]
            idx = i+1

    return maximum, idx


if __name__ == "__main__":
    a = [int(sys.stdin.readline()) for x in range(9)]
    maximum, idx = max_of(a)
    print(maximum)
    print(idx)

