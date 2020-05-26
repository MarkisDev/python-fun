"""
Tic Tac Toe
This script is a console version of Tic Tac Toe.
@author : MarkisDev
@copyright : https://markis.dev
"""  
import random
import os

# Function to initate and return TOSS.
def toss():
    t = random.choice(["0","1"])
    return t # 0 -> HEADS | 1 -> TAILS

# Function to initialize our grid
def init():
    global grid
    grid = [" "," "," "," "," "," "," "," "," "]
    global position
    position.clear()

# Function to accept P1 and P2 name and TOSS and begin with 1v1
def one():
    global cp1
    global cp2
    global p1
    global p2
    print("You have chosen 1v1")
    p1 = str(input("Please enter First Player's name: "))
    p2 = str(input("Please enter Second Player's name: "))
    print("\nWe shall now proceed with toss!\n")
    t = tossChooser(p1, p2)
    if (t == "win"):
        cp1 = str(input(p1 + " what do you want to play as? 'X' or 'O': ")).lower()
        if (cp1 == "x"):
            cp2 = "o"
        else:
            cp2 = "x"
    elif ( t == "loss"):
        cp2 = str(input(p2 + " what do you want to play as? 'X' or 'O': ")).lower()
        if (cp2 == "x"):
            cp1 = "o"
        else:
            cp1 = "x"
    else:
        print("You broke the code T_T\nPLEASE REPORT TO HAVE THIS FIXED ASAP\n OH! ALSO FUCK YOU xD")
        exit()

    print(p1 + " will be playing as " + cp1.upper() + "\n" + p2 + " will be playing as " + cp2.upper())
    init()

    if (t == "win"):
        print(p1 + " shall begin first!")
        onep1()
    elif (t == "loss"):
        print(p2 + " shall begin first!")
        onep2()

# Displaying Grid
def gridDisplay():
    global grid
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\t\t\t"+ "  " + grid[0] + "  |  " + grid[1] + "  |  " + grid[2])
    print("\t\t\t-----|-----|-----")
    print("\t\t\t"+ "  " + grid[3] + "  |  " + grid[4] + "  |  " + grid[5])
    print("\t\t\t-----|-----|-----")
    print("\t\t\t"+ "  " + grid[6] + "  |  " + grid[7] + "  |  " + grid[8])
    print("\t\t\t-----|-----|-----")

# ENDING MENU
def endMenu(p):
    if (p == p1):
        print(p1 + " WINS!")
    elif (p == p2):
        print(p2 + " WINS!")
    else:
        print("GOOD GAME GUYS! IT's A DRAW!!")

    choice = str(input("Enter 'YES' to play another game and 'NO' to quit: ")).lower()
    if (choice == "y" or choice == "yes"):
        one()
    else:
        exiter()

# Grid Checker for winner
def gridCheck(p):
    if (grid[0] == grid[1] == grid[2] and grid[0] != " " and grid[1] != " " and grid[2] != " "):
        endMenu(p)
    elif (grid[3] == grid[4] == grid[5] and grid[3] != " " and grid[4] != " " and grid[5] != " "):
        endMenu(p)
    elif (grid[6] == grid[7] == grid[8] and grid[6] != " " and grid[7] != " " and grid[8] != " "):
        endMenu(p)
    elif (grid[0] == grid[3] == grid[6] and grid[0] != " " and grid[3] != " " and grid[6] != " "):
        endMenu(p)
    elif (grid[1] == grid[4] == grid[7] and grid[1] != " " and grid[4] != " " and grid[7] != " "):
        endMenu(p)
    elif (grid[2] == grid[5] == grid[8] and grid[2] != " " and grid[5] != " " and grid[8] != " "):
        endMenu(p)
    elif (grid[0] == grid[4] == grid[8] and grid[0] != " " and grid[4] != " " and grid[8] != " "):
        endMenu(p)
    elif (grid[2] == grid[4] == grid[6] and grid[2] != " " and grid[4] != " " and grid[6] != " "):
        endMenu(p)
    else:
        if (grid[0] != " " and grid[1] != " " and grid[2] != " " and grid[3] != " " and grid[4] != " " and grid[5] != " " and grid[6] != " " and grid[7] != " " and grid[8] != " "):
         endMenu("draw")

# 1v1 Player 2 turn
def onep2():
    global position
    gridDisplay()
    gridCheck(p1)
    choice = str(input(p2 + " please enter your position: "))
    if (choice == "!"):
        exiter()
    elif (choice == "#"):
        instructions("p2") 
    elif (int(choice)-1 < 0 or int(choice)-1 > 8):
        print("ENTER VALID POSITION")
        onep1()
    elif int(choice)-1 in position:
        print("INVALID POSITION!")
        onep2()
    else:
        choice = int(choice) - 1
        grid[choice] = cp2
        position.append(choice)
        onep1()

# 1v1 Player 1 turn
def onep1():
    global position
    gridDisplay()
    gridCheck(p2)
    choice = str(input(p1 + " please enter your position: ")) 
    if (choice == "!"):
        exiter()
    elif (choice == "#"):
        instructions("p1") 
    elif (int(choice)-1 < 0 or int(choice)-1 > 8):
        print("ENTER VALID POSITION")
        onep1()
    elif int(choice) - 1 in position:
        print("INVALID POSITION!")
        onep1()
    else:
        choice = int(choice) - 1
        grid[choice] = cp1
        position.append(choice)
        onep2()

# Invalid choice handler for toss()
def tossChooser(p1, p2):
    t = toss()
    choice = str(input(p1 + " please choose 'HEADS' or 'TAILS': ")).lower()
    if (t == "0"):
         if(choice == "heads" or choice == "h" or choice == "0"):
            print(p1 + " WON THE TOSS!\n Better luck next time, " + p2)
            return "win"
         else:
            print(p2 + " WON THE TOSS!\n Better luck next time, " + p1)
            return "loss"
    
    elif (t == "1"):
        if (choice == "tails" or choice == "t" or choice == "1"):
            print(p1 + " WON THE TOSS!\n Better luck next time, " + p2)
            return "win"
        else:
            print(p2 + " WON THE TOSS!\n Better luck next time, " + p1)
            return "loss" 

    else:
        print("Invalid choice entered!")
        tossChooser(p1, p2)

# Instructions for the game
def instructions():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You have chosen instructions:")
    print("\t\t\t"+ "  " + "1" + "  |  " + "2" + "  |  " + "3")
    print("\t\t\t-----|-----|-----")
    print("\t\t\t"+ "  " + "4" + "  |  " + "5" + "  |  " + "6")
    print("\t\t\t-----|-----|-----")
    print("\t\t\t"+ "  " + "7" + "  |  " + "8" + "  |  " + "9")
    print("\t\t\t-----|-----|-----")
    print("\nThe player has to enter the number where he/she would like to place their mark. \n The one who gets 3 consecutive marks in linear directions, WINS\n!")
    menu()

# Quit the game
def exiter():
    print("You have chosen to exit the game")
    print('Thank you for playing, GGWP!')
    exit()

# Main menu 
def menu():
    print("\t\t Welcome to Tic Tac Toe")
    print("\t\t\t   - By Markis")
    print("\n\t\t1 - 1v1")
    print("\t\t# - Instructions")
    print("\t\t! - Exit game")
    menuChooser()
    
# Invalid choice handler for menu()
def menuChooser():
    choice = str(input("Please enter the appopriate option: "))
    if (choice == "1"):
        one()
    elif (choice == "#"):
        instructions()
    elif (choice == "!"):
        exiter()
    else:
        print("Invalid choice!\n")
        menuChooser()
cp1 = ""
cp2 = ""
p1 = ""
p2 = ""
grid = []
position = []
menu()
