a=input("enter parantesis:- ")
i=0
while i<len(a):
    if "()" in a:
        if len(a)%2==0:
           print("valid paranthesis")
        else:   
           print("invalid paranthesis")
        i=i+1