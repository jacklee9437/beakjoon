import re
from random import randint

bad = set(["씨발", "존나", "뻐큐", "fuck", "병신"])

while True :
    testword = input().rstrip()
    print(f"test target word is '{testword}'")

    testword = re.sub("[^a-zㄱ-ㅎ가-힣 ]", "", testword)
    testword = testword.split(" ")
     
    # 단어당 단일 for 문
    # if randint(0, 2) == 0 :
    #     print("test run")
    #     for word in testword :
    #         for i in range(1, len(word)+1) :
    #             if word[:i] in bad or word[i:] in bad: 
    #                 print(f"word is {word}, you are bad man!")
    
    # 단어당 투포인터 (이중 for문)
    if randint(0, 2) == 0 :
        print("test run")
        for word in testword :
            for i in range(0, len(word)-1) :
                for j in range(len(word), i, -1) :
                    if word[i:j] in bad: 
                        print(f"word is {word}, you are bad man!")

   
   