#a=[4,7,6,9,8,1,3]
import random
a=[]
c=0
def makeno():
    while len(a)<4:
        n = random.randrange(0,9)
        if n not in a:
           a.append(n)
    print(a)
    for i in range(10):
        x=0
        if x==0:
           pos,x=random.choice(list(enumerate(a)))
           print("number", x, "position",pos)
    if len(a)>len(set(a)):
       a.clear()
       makeno()
def playgame():
    global c
    c+=1
    cows=0
    bulls=0
    choice=int(input("enter no"))
    guess=[]
    for i in range(4):
        guess.append(int(choice[i]))
    for i in range(4):
        for j in range(4):
            if guess[i]==a[j]:
               cows+=1
    for x in range (4):
        if guess[x]==a[x]:
           bulls+=1
    print("bulls:",bulls)
    print("cows:",cows) 
    if bulls==4:
       print("you won win ",c,"c")
    #if bulls!=4:
    else:
        print("you looser") 
        playgame()
makeno()
playgame()                  



 




























