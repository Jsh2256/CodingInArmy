def d(n):
    temp=n
    total=0
    while True:
        total=n%10+total
        n=n//10
        if n<=0:
            break
    return total+temp

listA=[]
for i in range(0,10001):
    listA.append(i)
for i in range(0,10001):
    if d(i) in listA:
    	listA.remove(d(i))
for i in listA:
    print(i)