def get_marks():
    mark_array = []
    mark = int(input("Enter the mark or -1 to stop: "))

    while mark != -1:
        mark_array.append(mark)
        mark = int(input("Enter the marks: "))
    return mark_array

def print_list_size(mark_array):
    print(f"Our list has {len(mark_array)} elements")


def print_marks(mark_array):
    for x in range(len (mark_array)):
        print (f"Mark {x+1} is {mark_array[x]}")
    

def get_total(mark_array):
    total = 0
    for x in range(len(mark_array)):
        mark = mark_array[x]
        total = total + mark
        
        return total
    
def determine_highest(mark_array):
    highest = 0
    for i in range(len(mark_array)):
        current_mark = mark_array[i]
        if(current_mark>highest):
            highest = current_mark
        
        print(f"The highest of all marks = {highest}")
        
menu = "Press 1: Capture marks \n"
menu += "Press 2: Check number of marks\n"
menu += "Press 3: Get the sum marks\n"
menu += "Press 4: Get highest marks\n"

mark_captured = []
print(menu)
choice = int(input(": make your choice"))

while choice !=-1:    
    if choice == 1:
        mark_captured = get_marks()
        print(mark_captured)
    elif choice == 2:
        print_list_size(mark_captured)
    elif choice == 3 :
        calc_sum = get_total(mark_captured)
        print("The sum of all marks: ", calc_sum)
    elif choice == 4:
        determine_highest(mark_captured)
    else:
        print("not on the menu")
    
    print(menu)
    choice = int(input(": make your choice "))

