n=int(input("enter no"))
a = n
r=0
p=0
len1 = len(str(n))
i = 0
while(i<len1):
    r = n % 10
    p = p * 10 + r
    n = n//10
    i = i + 1
if a == p:
   print(p,"Number is Palindrome")
else:
   print("Number is not Palindrome")
    
    