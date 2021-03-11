# Mastermind - Simple Board Game
# @author : MarkisDev
# @copyright : https://markis.dev

import random
import sys
import time

def gen_colors(colors):
    question = []
    # Choosing 4 colors from the list (not unique)
    while True:
        if len(question) != 4:
            rint = random.randint(0,len(colors)-1)
            question.append(colors[rint])
        else:
            break
    # Shuffle list and return
    random.shuffle(question)
    return question

# Main program
def main():
    # Counter variables
    guesses = 0
    # Main list
    colors = ['red', 'green', 'blue', 'black', 'yellow', 'grey', 'magenta', 'white', 'violet', 'orange']
    print("Available colors list: ")
    print(', '.join(colors))
    # Generating question
    question = gen_colors(colors)
    print("Ans = ", question)
    while True:
        choice = input('Enter your color choice separated by space: ')
        choice_list = choice.lower().split()
        # Making sure user has entered 4 choices
        if len(choice_list) < 4 or len(choice_list) > 4:
            print(f"You have not entered 4 choices!")
            print("Restarting program...")
            time.sleep(3)   
            main()
        # Checking if all the entries are valid
        for choice in choice_list:
            if choice not in colors:
                print(f"You have entered an invalid color : {choice}")
                print("Restarting program...")
                time.sleep(3)   
                main()
        # Checking if all the choices are correct
        if choice_list == question:
            print(f"Congratulations! You win!\n Total Guesses: {guesses}")
            sys.exit()
        else:
            # Guess
            guesses +=1
            # Checking how many are correct in correct position
            correct_color, correct_place = 0,0   
            for i in range(4):
                # Correct color and place
                if choice_list[i] == question[i]:
                    correct_place += 1
                # Correct color, wrong place
                elif choice_list[i] in question:
                    correct_color +=1
            print(f"Correct color in correct place: {correct_place}")
            print(f"Correct color in wrong place {correct_color}")

if __name__ == '__main__':
    main()