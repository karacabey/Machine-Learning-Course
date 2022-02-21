import random as rd

number_of_x = 0
number_of_y = 0
counter = 0 # to control the loop

while(counter<1000):
    doors=["x","x","y"]
    
    rd.shuffle(doors) # shuffle the doors each time
    selected_index=rd.randint(0, 2) # user select a door
    selected_value = doors[selected_index] # selected value
    
    # after user selected a we need to determine a "x" that non-selected to remove
    for i in range(0,len(doors)):
        index_of_x = doors.index("x",i)
        if index_of_x != selected_index:
            break
    
    doors.pop(index_of_x) # remove the non-selected x 
    
    # user change your choice.
    if selected_value == "x":
        print("changed choice : y")
        number_of_y +=1
    else:
        print("changed choice : x")
        number_of_x +=1
    counter +=1

# print the number of choice result in 1000 times.
print("\nnumber of x : ",number_of_x)
print("\nnumber of y : ",number_of_y)


