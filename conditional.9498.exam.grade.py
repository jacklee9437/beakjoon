import sys

score = int(sys.stdin.readline())
if (90 <= score and score <= 100):
    print("A")
elif (80 <= score):
    print("B")
elif (70 <= score):
    print("C")
elif (60 <= score):
    print("D")
else:
    print("F")