#continuity of a function at a point
from sympy import Symbol,exp,sin,tan,Limit
x=Symbol('x')
y= Symbol('y')
h= Symbol('h')
#continuity
y=1/x
a=0
y1 = y.subs({x:a})
#The value of the function at a, ie  f(a)
print(y1)
q1 = y.subs({x:a+h}).evalf()
q2 = y.subs({x:a-h}).evalf()
#Left Hand Limit
t1 = Limit(q1,h,0).doit()
#Right Hand Limit
t2 = Limit(q2,h,0).doit()
print(t1,t2)
if(t1 == y1 and t2 == y1):
   print("Continous")
else:
     print("Not Continous")