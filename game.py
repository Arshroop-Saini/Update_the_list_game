
# Creating the main UI of the game 
def display():
    # Asking the user to pick up an index position
    position= "Somenting"
    in_range= False
    while position.isdigit()== False or in_range== False:
        position= input(("Pick up a position to replace (0,1,2): "))

        # Checking if the value that the user entered is a digit.
        if position.isdigit()== False:
            print("The position that you entered is not a digit, please enter a digit value!")
        
        # Checking if the digit value is in the specified range
        if position.isdigit()== True:
            if int(position) in [0,1,2]:
                in_range= True
            else:
                in_range= False
                print("The position you entered is not in the specified range, please entere the valid positon!")
    
    return int(position)

index=display()

#####################################################################################

# Asking the user to enter a value which he/she wants to replace the desired index with

def value():
    replace= 0
    while isinstance(replace, str)== False:
        replace= input("Type a String to replace at the position: ")

        if isinstance(replace, str)== False:
            print("Value that you entered is not a string, please enter a string")

    return str(replace)

    

replace_value=value()

#####################################################################################

# Adding the value entered by the user to the list

def adding(indece,value):
    list=[0,1,2]
    list[indece]=value
    return(f"Here is the Updated list {list} ")

final_list=adding(index, replace_value)
    
print(f"You updated list is {final_list}")

#####################################################################################

# Asking the user if he/she watns to play the game anymore, if in case bored :(
