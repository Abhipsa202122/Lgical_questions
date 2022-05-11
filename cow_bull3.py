import random
a1=input("enter your guess")
a2=input("enter your guess")
cows1=0
cows2=0
bulls1=0
bulls2=0
x=str(random.randint(1000,9000))
def cows_bulls():
    for i in x :
        print(i,x)   
        if i in a1:
           cows1=cows1+i

        else:
           bulls1=bulls1+i
        if i in a2:
           cows2=cows2+i
        else:
           bulls2=bulls2+i
        if cows1>=cows2:
           print("a1 wins")
        else:
           if cows2>=cows1:
              print("a2 wins")
           #if cows1==cows2:
             # print("same")

print("a1 cows are",cows1)
print("a1 bulls are ",bulls1)
print("a2 cows are",cows2)
print("a2 bulls are",bulls2)
print(x)
cows_bulls()
