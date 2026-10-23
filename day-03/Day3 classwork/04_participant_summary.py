fullname = input("Enter your name ")
name = fullname.strip().title()

staffnumber = input ("Staff number ")

level = input("enter your level ")

if name =="" or not staffnumber.isdigit() or not level.isdigit():
    print (" --------------  ")
    print ("Invalid Details entered")
    print (" --------------  ")

else:
    print (" --------------  ")
    print ("Summary of  Details entered")
    print ("          ")
    print("Name ", name)
    print ("Staff Number ", staffnumber)
    print ("Level ",level)
    print (" --------------  ")