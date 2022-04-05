import sys

a, b = sys.stdin.readline().split()
rev_a = int(a[::-1])
rev_b = int(b[::-1])
print(rev_a) if (rev_a > rev_b) else print(rev_b)