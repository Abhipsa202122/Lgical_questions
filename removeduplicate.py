n=[0,0,1,1,1,2,2,3,3,4]
i=0
a=[]
c=0
while i<len(n):
    if n[i] not in a:
       a.append(n[i])
       c+=1
    i+=1
print(c)
print(a)
#/p-5, nums = [0,1,2,3,4]        
