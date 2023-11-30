import random


class opcolor:
    GREEN = '\u001b[42m'
    YELLOW = '\u001b[43m'
    RED = '\u001b[41m'
    RESET = '\u001b[40m'


LISTSIZE = 1000
EXACT = 2
CLOSE = 1
WRONG = 0


def main():
#getting the size of the choice
    argument = int(input("Enter the wordsize from 5 to 8: "))
    if(argument == 5):
        wordsize = 5
    elif(argument == 6):
        wordsize = 6
    elif(argument == 7):
        wordsize = 7
    elif(argument == 8):
        wordsize = 8
    else:
        print("Error: wordsize must be either 5, 6, 7, or 8")
        return 1
    won = False
    rep = LISTSIZE*wordsize 
    x = random.randrange(0, rep, wordsize)
    #opening the file of words
    filename = str(wordsize) + '.txt'
    with open (filename, "r") as reader:
        if(reader == ''):
            print(f"Error opening file {filename}.\n")
            return 1
        else:
            casevar = reader.readlines(x)
            caselast = casevar[-1]
            choice = caselast.strip('\n') #getting the computers choice of words
    for m in range (wordsize):
        #function to get the guess from the user
        guess = get_guess(wordsize)
        #initializing the score checking array
        status = []
        for i in range (wordsize):
            status.append(WRONG)
        score = check_word(guess, wordsize, status, choice)

        print(f"Guess {m}:")

        print_word(guess, wordsize, status)

        if score == EXACT * wordsize:
            won = True
            break
    
    if won == True:
        print("You won!")
    else:
        print(f"The target word was {choice}. \nBetter Luck Next Time\n")
    return 0

   


def get_guess(wordsize):
#getting guess and making sure user inputs the correct value

    guess = input("Enter the input:")

    while(len(guess)!=wordsize):
        guess = input("Input a " + str(wordsize) + "-letter word: ")
    return guess.lower()


def check_word(guess, wordsize, status, choice):
#To keep track of exact, close and wrong values and give back a score
    score = 0
    for j in range (wordsize):
        if guess[j] == choice[j]:
            status[j] = EXACT
            score += 2
        else:
            for k in range (wordsize):
                if guess[j] == choice[k]:
                    status[j] = CLOSE
                    score += 1
                    break
                else:
                    status[j] = WRONG
    return score

def print_word(guess, wordsize, status):
    for n in range (wordsize):
        if status[n] == EXACT:
            print(f"\b{opcolor.GREEN}{guess[n]}{opcolor.RESET}", end=" ")
        elif status[n] == CLOSE:
            print(f"\b{opcolor.YELLOW}{guess[n]}{opcolor.RESET}", end=" ")
        else:
            print(f"\b{opcolor.RED}{guess[n]}{opcolor.RESET}", end=" ")
    print("\n")

main()
