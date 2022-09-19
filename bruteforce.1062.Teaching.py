from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
if K < 5 :
    print(0)
    exit(0)
K -= 5

learned = set("antic")
needToLearn = set()

for idx, word in enumerate(words) :
    words[idx] = set(word)
    needToLearn |= words[idx]
needToLearn -= learned
needToLearn = list(needToLearn)
if len(needToLearn) <= K :
    print(N)
    exit(0)

def dfs(idx, k) :
    if k == K :
        count = 0
        for word in words :
            if word.issubset(learned) :
                count += 1
        return count

    count = 0
    for i in range(idx, len(needToLearn)) :
        learned.add(needToLearn[i])
        count = max(count, dfs(i+1, k+1))
        learned.discard(needToLearn[i])
    return count

print(dfs(0, 0))