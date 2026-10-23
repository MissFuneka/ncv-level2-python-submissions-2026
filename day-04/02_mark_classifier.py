mark = input ("Enter the mark: ")
if mark != "":
    if mark.isdigit():#and mark > 100:
        mark = int(mark)
        if mark >= 0 and mark <=100:
            if mark >= 80:
                print ("Outstanding")
            elif mark >=70 and mark <80:
               print ("Highly Competent")
            elif mark >=60 and mark <70 :
                print ("Highly Competent")
            elif mark >=50 and mark <60:
                print ("Competent")
            elif mark >=40 and mark<=49:
                print ("Not Yet Competent ")
            
            else:
                print("Not achieved")
        else:
            print("Enter mark between 0 and 100")
    else:
        print("invalid mark")
else:
    print("No mark entered")