# Yet another Game
# Made by Hiferli
# Feel free to contact me for any mods
# NO CHEATING
# ~~~~~ 🎉 HOLA AMIGOS 🎉 ~~~~~s 

import random;

# Dev Options:
# Setting the difficulty level:

easyLevel = [1 , 10];
mediumLevel = [1 , 50];
hardLevel = [1 , 100];

difficulty = input("Enter your difficulty level (Easy/Medium/Hard): ").lower();

# Main Function
def guessWork(number , difficultyLevel):
    guessNumber = int(input("Enter your guess: "));
    numberOfGuesses = 0;

    while(guessNumber != number):
        if(guessNumber < difficultyLevel[-1] and guessNumber > difficultyLevel[0]):
            print("Incorrect guess :(. Please try again");
            if(guessNumber > number):
                print("Hint: Guess of a number smaller than this!! \n");
            else:
                print("Hint: Guess of a number greater than this!! \n");

            numberOfGuesses += 1;
            guessNumber = int(input("Enter your guess: "));
        else:
            print(f"Please enter a number within the difficulty level: {difficultyLevel[0]} to {difficultyLevel[-1]} \n");
            guessNumber = int(input("Enter your guess: "));

    numberOfGuesses += 1;
    print("Correct Guess...! You Won\n");
    print(f"You won after making {numberOfGuesses} guesses");

if(difficulty == 'easy'):
    print(f"Guess the number from the range: {easyLevel[0]} and {easyLevel[-1]}");
    number = random.randint(easyLevel[0] , easyLevel[-1]);
    print("Developer's Option: " + str(number));
    guessWork(number , easyLevel);

elif(difficulty == 'medium'):
    print(f"Guess the number from the range: {mediumLevel[0]} and {mediumLevel[-1]}");
    number = random.randint(mediumLevel[0] , mediumLevel[-1]);
    print("Developer's Option: " + str(number));
    guessWork(number , mediumLevel);

else:
    print(f"Guess the number from the range: {hardLevel[0]} and {hardLevel[-1]}");
    number = random.randint(hardLevel[0] , hardLevel[-1]);
    print("Developer's Option: " + str(number));
    guessWork(number , hardLevel);
