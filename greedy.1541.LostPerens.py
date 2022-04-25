from sys import stdin, maxsize
input = stdin.readline

sums = [sum(map(int,fml.split("+"))) for fml in input().rstrip().split("-")]
print(sums[0] - sum(sums[1:]))
