# declaration

mark_array = []
index = 0

mark = int(input("Enter the mark or -1 to stop: "))

while mark != -1:
    mark_array.append(mark)
    
    mark = int(input("Enter the marks: "))

print(f"Our list has {len(mark_array)} elements")



for x in range(len (mark_array)):
    print (f"Mark {x+1} is {mark_array[x]}")
    
total = 0
for x in range(len(mark_array)):
    mark = mark_array[x]
    total = total + mark
    
    avg = total / len(mark_array)

print("")
print(f"The sum of all marks = {total}")
print(f"The average of all marks = {avg:.2f}")


