
n=int(input())
isPrime=True
Pcount=0
listA=list(map(int,input().split()))
for i in listA:
    if i == 1:
        continue
    for j in range(2,i):
        if i%j==0:
            isPrime=False
        
    if isPrime==True:
    	Pcount+=1    
    
    isPrime=True
        

print(Pcount)
