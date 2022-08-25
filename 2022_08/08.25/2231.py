#sum(map(int,str(i)))
n=int(input())
Nstr=str(n)

nlenth=len(Nstr)
x=1
while True:
    total=0
    Xstr=str(x)
     
    for i in range(0,len(str(x))):
        total+=int(Xstr[i])
    total+=x
    if n==total:
        break
    if x>1000000:
        x=0
        break
    x+=1
    
print(x)
