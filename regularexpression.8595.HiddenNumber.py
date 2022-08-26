import re
from sys import stdin
input = stdin.readline

n = int(input())
word = input().rstrip()

hiddenNumbers = re.findall("[0-9]+", word)
print(sum(map(int,hiddenNumbers)))