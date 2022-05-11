import random
n=[]
c=0
def makeno():
    while len(n)<4:
        x = random.randrange(0,9)
        if x not in n:
            n.append(x)
    #for i in range(4):
     #   x=random.randrange(0,9)
     #   n.append(x)
    print(n)
        
if len(n)>len(set(n)):
    n.clear()
    makeno()
def playgame():
    global c
    c+=1
    cows=0
    bulls=0
    #print(n)
    choice=input("enter no a 4 digit no")
    guess=[]
    for i in range(4):
        guess.append(int(choice[i]))
    for i in range(4):
        for j in range(4):
            if guess[i]==n[j]:
               cows+=1
    for x in range (4):
        if guess[x]==n[x]:
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