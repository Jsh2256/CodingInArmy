x=int(input())
listSub=[]
count=0
isTrue=False
for i in range(1,x+1):
    listA=list(map(int, str(i)))
    if i<100:
        count+=1
    elif listA[0]-listA[1]==listA[1]-listA[2]:
        count+=1
        
print(count)