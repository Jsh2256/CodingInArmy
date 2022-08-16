m,n=map(int, input().split())

numbers=[]

for i in range(0,n+1):
    numbers.append(i)

for i in range(2, n+1):
    if numbers[i]==0:
        continue
    for j in range(2, n//i+1):
        numbers[i*j]=0

for i in range(2, n+1):
    if i < m:
        del numbers[i]
        
        
        
for i in range(2, len(numbers)):
    if numbers[i]!=0:
        print(numbers[i])

        
        