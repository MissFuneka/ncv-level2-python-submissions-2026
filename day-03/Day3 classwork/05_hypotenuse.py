# hypoteneuse of a right angled triangle

import math

#declare variables Two sides of a right angle triangle

adjacent_side = float (input("Adjacent Side  (metres): "))
opposite_side = float ( input (" Opposite side (metres): "))

#check that the right values are entered
if adjacent_side <= 0:
    print("")
    print ("Adjacent side must be greater than 0")

else:
    if opposite_side <= 0:
        print("")
        print ("Opposite side must be greater than 0")
    else:
            adjacent_side_squared=math.pow(adjacent_side,2)
            opposite_side_squared = math.pow(opposite_side,2)
            hypotenuse = math.sqrt(adjacent_side_squared + opposite_side_squared)
            print("")
            print(f"The hypotenuse: {hypotenuse:.2f} m")
           