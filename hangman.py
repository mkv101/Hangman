

# my hoe program
def main():
    secretWord = "water"
    print("What is your guess?")
    letterGuess = input()

    if letterGuess == secretWord:
        print("correct")
    else:
        while (letterGuess != secretWord):
            print("What is your guess?")
            letterGuess = input()

    # complete = 0
    # while complete != 5: 
    #     print(complete)
    #     #add one each time 
    #     complete += 1

    



if __name__ == "__main__":
    main()