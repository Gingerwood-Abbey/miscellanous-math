#checking whether a function is differentiable or not
from sympy import * 
x = Symbol('x')
y = Symbol('y')
h = Symbol('h')
y = 1/x
s1 = y.subs({x:x+h}).evalf()
s2 = y.subs({x:x-h}).evalf()
# first derivative principle ie f'(x) = lim h->0 (f(x+h) - f(x))/h
z1 = Limit((s1-y)/h,h,0).doit() # Left Hand Derivative
z2 = Limit((s2-y)/h,h,0).doit() # Right Hand DErivative
print("LHD=",z1,"\nRHD=",z2)
if(z1 == z2):
   print("Function is differentiable")
else:
     print("Function is not differentiable")
