#import time
def fibbonacci(n):
    if n<3:
        return n-1
    return fibbonacci(n-1) + fibbonacci(n-2)
def fibbonacci_optimized(n):
    a=0
    b=1
    if n==1:
        return a
    if n==2:
        return b
    cnt=2
    while cnt<n:
        a,b=b,a+b
        cnt+=1
    return b

#t0= round(time.time(),4)
#print(fibbonacci_optimized(45))
#t1= round(time.time(),4)
#print(round(t1-t0,3))
#print()
#print(fibbonacci(45))
#t2= round(time.time(),4)
#print(round(t2-t1,3))
#
#701408733
#0.0
#701408733
#103.103
