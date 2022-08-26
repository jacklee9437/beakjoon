from operator import truediv
from sys import stdin
input = stdin.readline

N = int(input())
cards = list(map(int,input().split()))
cards.sort()

M = int(input())
check = list(map(int,input().split()))

def bisearch(n) :
   global N
   left = 0
   right = N-1
   while left <= right :
      mid = (left + right) // 2
      if cards[mid] > n :
         right = mid - 1
      elif cards[mid] < n :
         left = mid + 1
      else :
         return True
   return False

ans = [1 if bisearch(i) else 0 for i in check]
print(*ans)