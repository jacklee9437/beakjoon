from sys import stdin
input = stdin.readline

N, K = map(int,input().split())
words = [set(input().rstrip()) for _ in range(N)]
words.sort(key=lambda x : len(x))

learned = set("antatica")
if K < len(learned) :
   print(0)
   exit(0)

count = 0
for w in words :
   need_word = w - learned
   need_len = len(need_word)
   if (len(learned) + need_len <= K) :
      for nw in need_word :
         learned.add(nw)
      count += 1

print(count)
