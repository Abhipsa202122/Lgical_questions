import random
name=input("enter your name")
print("welcome to HANGMAN GAME! ", name)
words=["hangman","login","signup","cowsbulls"]
hang=[
    """
       +----+
            |
            |
            |
            |
            ===""","""
       +----+
         |  |
         o  |
            |
            |
            ===""","""
        +----+
           | |
           o | 
           | |
             |
             ===""","""
        +----+
           | |
           o | 
          /|\| 
             |
             ===""","""
        +----+ 
           | |
           o | 
          /|\|
          / \|
             ===""","""        
        +----+ 
           | |
           | |
           o | 
          /|\|
          / \|
             ==="""
             ]        
a=random.choice(words)
print("Guess a characters")
guesses=''
turns=6
i=1
while turns>0:
    failed=0
    for char in a:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            print(char,end=" ")
            failed += 1
             
    if failed==0:
        print("You Winner")
        print("The word is: ",a)
        break
    print()
    b=[]
    count=0
    for  char in range(turns):
        guess = input("guess a character:")
        guesses += guess
        if guess not in a:
            char+=1
            count+=1
            turns-=1
            b.append(char)
            print(hang[char])
            print("Wrong",count)
            print("You have", count, 'more guesses')

        if count == turns-1:
           print("You Looser")
           break
    if failed==0:
       #print("You Looser")
       break
    elif count==turns-1:
        break