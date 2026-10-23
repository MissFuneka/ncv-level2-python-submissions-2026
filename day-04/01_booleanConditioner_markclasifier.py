mark = input("Enter a mark ")

if mark.isdigit():
    mark = int(mark)
    if mark >= 0 and mark <= 100:
        if mark >= 50:
            if mark >=75:
                    print ("You passed and got a distinction")
            else:
                print ("You have passed")
        else:
                print("You have failed")
    else:
        print ("enter mark between 0 and 100")
else:
    print("invalid mark entered")