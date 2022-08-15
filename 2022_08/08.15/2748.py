def fibo(n):
    if memo[n]>0:
        return memo[n]
    if n>1:
        memo[n]=fibo(n-1)+fibo(n-2)
        return memo[n]
    else:
        return memo[n]
        
        

memo=[]
n=int(input())
for i in range(0,n+1):
    memo.append(0)
memo[1]=1
memo[0]=0
print(fibo(n))