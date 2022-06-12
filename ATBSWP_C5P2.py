# Fantasy Game Inventory (Chapter 5, Project 2)
# Automate the Boring Stuff With Python

'''
Question
Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
'''
# Imports and supports

# Define the function
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        item_total += 1
    print('Total number of items: ' + str(item_total))
    
# Define the dictionary
stuff = {'rope': 1, 'torch': 6, 'gold coins': 42, 'dagger': 1, 'arrow': 12}

# Call the function
displayInventory(stuff)