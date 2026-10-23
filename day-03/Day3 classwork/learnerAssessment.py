#Program that calculates the students PLP marks fo entry into Ncv courses 
#declaring variables
name= input("Enter name: ")
icass_mark = input("Enter the Icass Mark: ")
practical_test = input("Enter the Practical Test: ")
exam_mark = input("Enter the exam mark: ")

nameCleared = name.strip().title() #cleaning the text

#check that the correct values are entered
if name =="" or name.isdigit() or not icass_mark.isdigit() or not practical_test.isdigit() or not exam_mark.isdigit():
    print("Enter valid name or marks: ")
else:
        #converting strings to  integers
        icass_mark = int(icass_mark)
        practical_test = int(practical_test)
        exam_mark = int(exam_mark)
        
        #Calculating the final Mark
        finalmark = 0.3*icass_mark + 0.4*practical_test + 0.3*exam_mark
        #Check for boundary values
        if 0 <= icass_mark<=100 and 0<=practical_test<=100 and 0<= exam_mark<=100:
            if finalmark >= 50:
                print (f"Your final is : {finalmark:.0f} %")
                print(nameCleared," ","You have qualified for NCV Level 2")
            else:
                print (f"Your final is : {finalmark:.0f}%") #Messa
                print(nameCleared," ","Unfortunately, You have not qualified for NCV Level 2")    
        else:
            print("Marks cannot be smaller than 0 or bigger than 100") #Error Message for boundary values

