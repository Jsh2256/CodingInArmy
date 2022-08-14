n=1
target=int(input())
total=1
while True:
    if target==1:
        n=2
        break
    if total>=target:
        break
    total=total+6*(n-1)
    n=n+1
    
print(n-1)