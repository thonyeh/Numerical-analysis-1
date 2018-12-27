from sympy import *
from math import *
x= symbols('x')
init_printing(use_unicode=True)
f=raw_input('f(x)=')
g=diff(f,x)
print 'g(x)=',g
