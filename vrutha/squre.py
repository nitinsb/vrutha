import math 

# let c1 be the circle whose diameter is the same as the diagonal of the square
# let c2 be the circle whose radius is the same as the diagonal of the square
d = int(input("..Enter the area of a circle..."))
root = math.sqrt(d)
if int(root + 0.5) ** 2 == d:
    print(d, "is valid")
else:
    print(d, "it's not valid")
    exit(0)


x = 2*d ** 0.5 # x <- diagonal of sqare  = [ ((root 0f 2 ) * side) ]   or { root(area * 2) }
print("Area of circle c1 is ...",math.pi*((x/2)**2))

print("Circumferance of circle c2 is ...",math.pi*2*x)

