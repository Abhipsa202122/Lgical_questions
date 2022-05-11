import json
print("welcome to Login/signup")
user=input("LOGIN/SIGN-UP")
username=input("Enter your e-mail or mobile no:")
password=input("Enter your password:")
password1=input("enter confirm password")
if password==password1:
   print("both password should be same")
else:
   print("both are not same")    
gen=input("Enter your Gender")
if gen=="male" or gen=="female":
   print(gen)
   d={}
   l=[]
   l1=[]
   for i in range(len(user)):
       #l.append(user)
       l.append(username)
       l1.append(password)
       #l.append(gen)
       '''d={}
       for i in l:
           for j in l1:
               l[i]=j
               l1.remove(j) '''  

       '''for j in range(len(username)):
           d[username[j]]=password[i][j]'''
         #d.update({password[i]:d1})
       
print(l)
print(l1)
d={}
for i in l:
    for j in l1:
        d[i]=j
        l1.remove(j) 
print(d)         


   #print(l)   
with open("user_details.json","w") as file:
   json.dump(l,file,indent=4)
   for i in file:
       a,b = i.split(",")
       b = b.strip()
       if a==username and b==password:
          success=True
          break
   file.close()
   if(success):
      print("Login Successful")
      
   else:
      print("wrong user name or password please try again")
