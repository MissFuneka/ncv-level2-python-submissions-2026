##import math

n = int (input("enter number: "))
if n !=0:
    print("")
    totale = 0   
    for x in range(1,n+1):
        cube = x**3
        print(cube, end=" ")
    
        totale = totale +cube
    print("")
    print("")
#print (f"The total is "{totale: .0f}")

    print (f"The total number is: {totale:.0f}")
else:
    print ("number cannot be 0")

