#limit of a function
from sympy import *
x = Symbol('x')
#function
y= tan(x)/x
pprint(y)
pprint(limit(y,x,0))
