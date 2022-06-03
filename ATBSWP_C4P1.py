# Comma Code (Chapter 4, Project 1)
# Source: Automate the Boring Stuff With Python

'''
Question
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with 'and' inserted before the last item. 
'''

# Defining the function
def comma_code(items):
    item_length = len(items) # Define the length of the list.

    if item_length == 0:
        print("There are no items on the list.")
    elif item_length == 1:
        print("There is one item on the list: " + items[0])
    else:
        print("There are many items on the list: " + ", ".join(items[:-1]) + ", and " + items[-1], end = ".")
        # Used the join method -- struggled to find the right way to do this, but this is easier.

# Set the list
spam = ["apples", "bananas", "tofu", "cats"]

# Running the function
comma_code(spam)
