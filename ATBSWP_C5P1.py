# Chess Dictionary Validator (Chapter 5, Project 1)
# Automate the Boring Stuff With Python

'''
Question
Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.
Notes: Board grid is 1a to 8h; pawn (8), knight (2), bishop (2), rook (2), queen (1), king (1); bking, wking
'''

# Define the function
def isValidChessBoard():
    
    # Determine the piece to move
    print("What piece would you like to move?")
    piece = input()
    while piece not in thePieces:
        print("Invalid piece. Try again. Your options are: " + str(thePieces) + ".")
        piece = input()
    print("Valid piece.")        

    # Determine the starting spot
    print("Where are you moving " + piece + " from?")
    startLoc = input()
    while startLoc not in theBoard.keys(): # Determines if this spot is on the board.
        print("That is not a valid spot. Please try again. Your options are: a1:h8.")
        startLoc = input()
    while (startLoc,piece) not in theBoard.items(): # Determines if this spot has the selected piece on the board.
        print(piece + " is not located on " + startLoc + ". Please review the current board setup for " + piece + " and try again.")
        for key,value in theBoard.items():
            if piece == value:
                print(piece + " is located at " + key)
        startLoc = input()
    print("Valid: " + piece + " is at " + startLoc + ".")

    # Determine the ending spot
    print("Where would you like to move" + piece + "?")
    endLoc = input()
    while endLoc not in theBoard.keys():
        print("That is not a valid spot. Please try again. Your options are a1:h8.")
        endLoc = input()
    print("You're lucky I don't know how to code the right moves, but at least you got a spot on the board.")

# Define the dictionaries and lists
theBoard = {'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen', 'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
            'a7': 'bpawn', 'b7': 'bpawn', 'c7': 'bpawn', 'd7': 'bpawn', 'e7': 'bpawn', 'f7': 'bpawn', 'g7': 'bpawn', 'h7': 'bpawn',
            'a6': '', 'b6': '', 'c6': '', 'd6': '', 'e6': '', 'f6': '', 'g6': '', 'h6': '',
            'a5': '', 'b5': '', 'c5': '', 'd5': '', 'e5': '', 'f5': '', 'g5': '', 'h5': '',
            'a4': '', 'b4': '', 'c4': '', 'd4': '', 'e4': '', 'f4': '', 'g4': '', 'h4': '',
            'a3': '', 'b3': '', 'c3': '', 'd3': '', 'e3': '', 'f3': '', 'g3': '', 'h3': '',
            'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn', 'd2': 'wpawn', 'e2': 'wpawn', 'f2': 'wpawn', 'g2': 'wpawn', 'h2': 'wpawn',
            'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen', 'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook'}
            
            # Brute forced the dictionary setup. Must be a way to autogenerate these dictionary keys/board locations? [a-h][1-8]

thePieces = ["wpawn", "wrook", "wknight", "wbishop", "wqueen", "wking", "bpawn", "brook", "bknight", "bbishop", "bqueen", "bking"]

theNewBoard = {} # Placeholder list -- can be modified by a new function that will action the move that is validead by isValidChessBoard() -- maybe use copy/deepcopy?

# Call the function
isValidChessBoard()
