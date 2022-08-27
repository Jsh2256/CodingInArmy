#intertools 순열과 조합
import itertools
n=int(input())
listN=[int(x) for x in input().split()]
per_listN=itertools.permutations(listN)
result=0
max=result
for i in per_listN:
    for j in range(0,n-1):
        result=abs(i[j]-i[j+1])+result
    if max<result:
        max=result
    result=0
print(max)