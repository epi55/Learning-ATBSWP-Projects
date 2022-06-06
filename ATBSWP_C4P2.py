# Coin Flip Streaks (Chapter 4, Project 2)
# Source: Automate the Boring Stuff With Python

'''
Question
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails.
'''

# Imports and global variables and lists
import random
numberOfRolls = 0
numberOfStreaks = 0
flipRecord = []
flipRecordString = ()

# Define functions
def flip100():
    count = 0
    while count < 100:
        currentFlip = random.randint(0,1) # Assumption: 0 = Heads, 1 = Tails.
        flipRecord.append(currentFlip)
        count += 1
        global numberOfRolls # For feedback when running function
        numberOfRolls += 1
    print("flip100 executed. Roll number: " + str(numberOfRolls))

def flip100Review():
    # Convert from list to string type (I don't know how to find patterns in lists)
    flipRecordString = ''.join([str(item) for item in flipRecord])

    # Find pattern
    countHeads = 0
    countTails = 0
    countHeads = flipRecordString.count("000000") # Look for six sequential Heads
    countTails = flipRecordString.count("111111") # Look for six sequential Tails

    # Print to see results
    print("Six sequential Heads: " + str(countHeads))
    print("Six sequential Tails: " + str(countTails))

    # Add results to numberOfStreaks
    global numberOfStreaks
    numberOfStreaks += countHeads + countTails

# Call functions
for experimentNumber in range(10000):
    flip100()
    flip100Review()
    flipRecord = []
    flipRecordString = ()
print("Combined Heads and Tails: " + str(numberOfStreaks))
print("Chance of streak: " + str(numberOfStreaks / numberOfRolls * 100) + "%")
## print("Chance of streak: %s%%" % (numberOfStreaks / 100)) # Sample code was provided, but I'm not sure it does because it wasn't producing the right percentages as I increased the experimentNumber range.