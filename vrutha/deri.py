from sympy import *
x, y, z  ,x1, y1, z1, x2 ,y2, z2, x3, y3, z3, L= symbols('x y z x1 y1 z1 x2 y2 z2 x3 y3 z3 L')
init_printing(use_unicode=True)
"""
REFERANCE :- for derivation given in NCERT
funtion given in ncert text-book
consider that function 
lambada = 'L'
f(x,y,z) = (x1x+y1y+z1z)+L((x2-x1)x+(y2-y1)y+(z2-z1)z) = 0
further deriving the same fuction we end up in the given funtion refer the textbook 3d
 f(x,y,z) = (x1-L(x2-x1))x+(y1-L(y2-y1))y+(z1-L(z2-z1))z.

    now  u can represent that fnction as 
    f(x,y,z) = (x1-L(x2-x1))x+(y1-L(y2-y1))y+(z1-L(z2-z1))z.
    let a(x1,y1,z1) and b(x2,y2,z2) be a given points and we will derive parial derivitives between these points
"""
# initilise a functions
f = (x1+L*(x2-x1))*x+(y1-L*(y2-y1))*y+(z1+L*(z2-z1))*z;
# pariall derivation with x
f_x= diff(f, x)

# pariall derivation with y
f_y= diff(f, y)

# pariall derivation with z
f_z= diff(f, z)



print(f_x)
print("With partial derivation with respect to x ..",f_x)
print(f_y)
print("With partial derivation with respect to y ..",f_y)
print(f_z)
print("With partial derivation with respect to z ..",f_z)


# initially set lamada value to 0
L = 0
#Reading a(x1,y1,z1) and b(x2,y2,z2)
print("Enter the co-ordinates of point a")
x1,y1,z1 = map(int, input().split())
print("Enter the co-ordinates of point b")
x2,y2,z2 = map(int, input().split())



# to find all derivative between two points a,b will use f_d from 
# for small tiny steps Lambda = 0.001 i.e lim(Lambda) ---> 0(zero)
 
while L < 1.001:
    print([L*(-x1 + x2) + x1, L*(-y1 + y2) + y1, L*(-z1 + z2) + z1])
    L += 0.001 