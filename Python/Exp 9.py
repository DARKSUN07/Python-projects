import sympy
from sympy import symbols
from sympy import sin,cos,pi,expand,factor,Rational,diff,exp,re,im,I,simplify,Integral,Eq,integrate,oo,limit,solve
x, y =symbols('x y') 
x=sympy.sqrt(3) 
print(x) 
a0,a1,a2,a3,a4=symbols('a:5') 
a3=a1+2*a2 
sympy.pprint(a3) 

expr= cos(x)*cos(x)+sin(x)*sin(x)
z=expr.evalf(subs={x:pi/4,y:pi/4})
print(z)

expr=y*y+4*y+4
z=factor(expr)
sympy.pprint(z)
ez=expand(z); print("\n")
sympy.pprint(ez)

x,t,z,nu =symbols('x t z nu')
exd=diff(sin(x)*exp(x), x)
print("Simple print representation:",exd,"\n")
print("Pretty_print output:")
sympy.pprint(exd)

m,n,a,b,x=symbols('m n a b x')
expr= (a*x + b)**m
dexpr=expr.diff( (x , n) )
sympy.pprint(dexpr)

sympy.pprint(Integral(cos(x)**2,(x,0,pi)));print("\n")
sympy.pprint(integrate(cos(x)**2,(x,0,pi)));print("\n")
sympy.pprint(Integral(cos(x)**2,(x,-oo, oo)))

print(limit(sin(x)/x,x,0))

sympy.pprint(solve(x**2, -2,x))

eq1=Eq(2*x -y,1)
eq2=Eq(x + y,5)

sol = solve((eq1,eq2),(x,y))
print(sol,"\n")
print(f'The solution is x= {sol[x]}, y= {sol[y]}')

print(simplify(sin(x)**2 + cos(x)**2),"\n")
sympy.pprint(simplify(2*cos(x)**2-1))


c1=3+4*I 
c2=complex(4,5) 
c3=sympy.sqrt(-1) 
sympy.pprint(c2) 
sympy.pprint(c3) 
sympy.pprint(c1+c2) 
print("Real part of cl : ",re(c1)) 
print("Imaginary part of ci : ",im(c1)) 
print("Absolute value of c2 : ",abs(c2)) 
print("Conjugate of ci : ");sympy.pprint(c1.conjugate()) 

a=Rational(3,4) 
print(a) 
print(a.p,"/",a.q,"\n") 
b=Rational('0.75') 
print(b,"\n") 
c=Rational(0.75) 
print(c,"\n") 
d=Rational(2,3) 
e=Rational(10,30) 
print(e,"\n") 
f=Rational(169,260) 
print(f.p,"/",f.q) 
print(f)
