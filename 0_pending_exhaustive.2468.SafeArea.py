from sys import stdin, maxsize
input = stdin.readline




N = int(input())
inputArr = tuple(tuple(map(int,input().split())) for _ in range(N))


max = -maxsize

