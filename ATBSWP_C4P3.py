# Character Picture Graph (Chapter 4, Project 2)
# Source: Automate the Boring Stuff With Python

'''
Question
Copy the previous grid value, and write code that uses it to print the image [rotated by 90 degrees clockwise to be a heart top-bottom, not left-right].
'''

# Define the function
def picture_graph(pic):
    for i in range(len(pic[0])):
        for j in range(len(pic)):
            print(pic[j][i], end = '')
        print()

'''
I didn't successfully define the function without looking at an example.
I was confused by how to start; this example is very clear cut via ranges.
Still trying to think through the logic here.
i = 6 (the length of a sub-list) (only works if sub-lists are the same length)
j = 9 (the number of sub-lists)
Order of operations to print must be: 0,0 - 1,0 - 2,0 - 3,0
How to remember the order of nested ranges?
1-The highest range locks in the first iteration.
2-The lowest range then iterates through all its variables
3-The higest range locks in the second iteration.
4-The lowest range then iterates through all of its variables again.
5-Etc.
So determine HOW you want to print, then figure out the high/low range iteration pattern.
'''

# Define the list
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Call the function
picture_graph(grid)
