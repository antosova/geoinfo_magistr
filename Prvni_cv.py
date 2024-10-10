from math import *
#coeficients
a=6
b=5
c=1
#diskriminant
D=b**2 - 4*a*c

#Counting root x1, x2 if D>0
if D > 0:
    x1 = (-b + D**(1/2))/(2*a)
    x2 = (-b - sqrt(D))/(2*a)
    print("Two roots, x1=",x1,"x2",x2)
#Counting roots x1=x2, if D=0   
elif D ==0:
    x1 = (-b)/(2*a)
    print("x1=x2",x1) 
# Counting roots x1=x2, if D<0    
else:
    print("no solution in R")
    
# DÚ nalézt maximum ze 3 čísel a b c using defined function

#while cyklus, třeba faktoriály...n!=n(n-1)!,n>1
#n=12
#fn = 1
#while n>1
#fn = n*f*n
#n=n-1
n = 12
fn = 1
while n>1:
    fn=fn*n
    n=n-1 
    
print("n!=",fn )



