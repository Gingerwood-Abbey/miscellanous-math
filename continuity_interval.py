#continuity of function at an interval
from sympy import *
from numpy import arange
x = Symbol('x')
y = Symbol('y')
h = Symbol('h')
y = x**2
is_continous = True
a =1
b =4
#checking the continuity in the interval a,b
for c in arange(a,b,0.5):
   y1 = y.subs({x:c}).evalf()
   q1 = y.subs({x:c+h}).evalf()
   q2 = y.subs({x:c-h}).evalf()
   w1 = Limit(q1,h,0).doit()   # Left Hand Limit - LHL
   w2 = Limit(q2,h,0).doit()   # Right Hand Limit - RHL
   if (y1 != w1 and y1 != w2): #checking if  LHL is equal to RHL
      is_continous = False
      break
if is_continous: 
   print(" The function is continous")
else:
     print(" The Function is not continous ")