#checking whether a function is differentiable or not in an interval
from sympy import *
from numpy import arange
x= Symbol('x')
y = Symbol('y')
h = Symbol('h')
y = x**2 # function
is_differentiable = True
# The intervals
a= 1
b = 4
for c in arange(a,b,0.1):
   s1 = y.subs({x:x+h}).evalf() 
   s2 = y.subs({x:x-h}).evalf()
   w1 = Limit((s1-y)/h,h,0).doit() # LHD
   w2 = Limit((y-s2)/h,h,0).doit() #RHD
   if w1 != w2:
     is_differentiable = False
     print(w1,w2)
     break
if is_differentiable:
  print("The Function is differentiable")
else: 
     print("The Function is not differentiable")