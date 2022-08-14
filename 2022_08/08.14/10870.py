fn2=0
fn1=1
target=int(input())

fn=0
if target >= 2 :
    for i in range(0,target-1):
    	fn=fn1+fn2
    	fn2=fn1    
    	fn1=fn
elif target==1:
    fn=1
    
else :
    fn=0
     
print(fn)