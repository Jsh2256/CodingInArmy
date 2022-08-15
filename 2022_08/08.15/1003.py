def fibo(n):
    if memo[n]>0:
        return memo[n]
    if n>1:
        memo[n]=fibo(n-1)+fibo(n-2)
        return memo[n]
    else:
        return memo[n]
        

testcase=int(input())
for i in range(testcase):
    memo=[]
    n=int(input())
    for i in range(0,n+2):
    	memo.append(0)
    memo[1]=1
    memo[0]=0
    fibo(n)
    print(memo[n-1],memo[n])
    
