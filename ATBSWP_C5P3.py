# List to Dictionary Function for Fantasy Game Inventory (Chapter 5, Project 3)
# Automate the Boring Stuff With Python

'''
Question
Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the players inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item.
'''

# Imports and supports

# Define the functions
def displayInventory(inventory):

    print('Inventory:')
    item_total = 0

    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        item_total += v
    
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):

    updatedInventory = dict(inventory)

    for item in addedItems:
        updatedInventory.setdefault(item, 0)
        updatedInventory[item] += 1
    
    return updatedInventory

# Define the dictionaries and lists
inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Call the function
updatedInventory = addToInventory(inventory, dragonLoot)
displayInventory(updatedInventory)
