from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

def check(val) :
   global M
   cnt = 0
   length = 0
   ret = 0
   for lesson in lessons :
      if length + lesson > val :
         cnt += 1
         length = lesson
         continue
      length += lesson
   if length != 0 :
      cnt += 1

   if cnt > M :
      return True
   else :
      return False

ret = 0
left = max(lessons)
right = sum(lessons)

while left < right :
   mid = (left + right) // 2

   if check(mid) :
      left = mid + 1
   else :
      ret = mid
      right = mid - 1

print(ret)
