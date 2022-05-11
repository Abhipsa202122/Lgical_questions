import random
n=str(random.randint(0,9))   
cow=0
guess=1
def count(guess_no):
    cows=0
    bulls=0
    for i in range(0,4):
        if guess_no[i]==n[i]:
           cows+=1
        elif guess_no[i] in n:
            bulls+=1
    return cows,bulls
if __name__=="_main_":
    while cow<4:
        a=input("enter no")
        cow,bulls=count(a) 
        print("cows",cow)
        print("bulls",bulls) 
        if cow==4:
           print("congts",n)
        else:
           guess+=1                  
