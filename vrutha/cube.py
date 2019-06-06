n = int(input("Enter the number of cubes....  "))
#cheacking if n is valid
f = 0
for i in range(1 , n+1):
    if i**3 == n:
        f = 1 # flag variable seeting to 1 if it is a perfect cube.
        print("Valid length..")
        break

if f == 0:
    print("Invalid entry ...")
else:
    print("The surface area before removing corner cubes ",i*i*6)
    if(n == 1 or n == 8):
        print("The surface area is ",0)
    else:
        print("The surface area after removing corner cubes ",i*i*6)
        print("Conclusion : If N is nither 1 nor 8 then surface area of both cases that after removing the corner pieces and before removing corner pieces is same.... ")

        

