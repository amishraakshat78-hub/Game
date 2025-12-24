import random
print("-Hey! this side is interesting ")
name=input("What is your name? :")
print("Good luck, ",name)
words=["red","green","blue","orange","pink","silver","golden","white","black","violet","brown","purple","yellow","grey"]
word=random.choice(words)
x=len(word)
print("Guess ",x," words colour name")
guess=' ' 
turns=10
while turns>0:
    failed=0
    for char in word:
        if char in guess:
            print(char,end=" ")
        else:
            print("_")
            failed+=1
    if failed==0:
        print("Great! You win :) ")
        print("The word is ",word)
        break
    print()
    guessw=input("Guess a character:")
    guess+=guessw
    if guessw not in word:
        turns-=1
        print("Try again wrong ")
        print("You have +",turns,"more guesses")
        if turns==0:
            print("You loose !,Better luck next time")
