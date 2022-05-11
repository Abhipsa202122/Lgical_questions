def f(b):
    d=[1,5,10,50,100,500,1000]
    r=["I","V","X","L","C","D","M"]
    rd=""
    i=0
    while b>0:
         for i in range (b//d[i]):
            rd+=r[i]
            b-=d[i]  
         i+=1
print(f(1500))         