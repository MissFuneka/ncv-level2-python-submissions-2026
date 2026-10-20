first_number = int( input("First number: ")) 
second_number = int ( input ("Second Number: "))

if first_number < second_number :
    factor = first_number

else:
    factor= second_number
    
while first_number % factor != 0 or second_number % factor !=0:
    factor = factor - 1

print ("The highest common factor is" , factor)
