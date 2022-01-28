# This is a Snake Water Gun Game
# This is made by Hiferli
# This is just a sample project
# Feel free to suggest any changes

# Github: /hiferli
# ~~~~~~~~ 🎉 HOLA AMIGOS 🎉 ~~~~~~~~

import random

options = ["Snake" , "Water" , "Gun"];
computer = random.choice(options);
# print(computer);

print("Welcome to the Snake Water Gun Game...");
# print(''' Rules: 
#     --> You can choose your fighter from any one of Snake🐍, Water🌊 and Gun🔫.
#     1.) Winning Conditions:
#         a.) Snake🐍 will win from Water🌊
#         b.) Water🌊 will win from Gun🔫
#         c.) Gun🔫 will win from Snake🐍.
#     2.) Tie Conditons:
#         ~ When both the options choosen by the user and the computer are the same, the match becomes a tie.
#     3.) Loosing Conditions:
#         ~ All the other combinations would make you loose the game.

# ''')
userOption = input("Enter your option: ");
print("You choose: " + userOption.capitalize());
print("The computer chooses: " + computer);

result = None;

if(userOption == "Snake" or userOption == "snake"):
    if(computer == "Snake"):
        result = 0;
    elif(computer == "Water"):
        result = 1;
    
    else: 
        result = -1;
        

elif(userOption == "Water" or userOption == "water"):
    if(computer == "Snake"):
        result = -1;
    
    elif(computer == "Water"):
        result = 0;
    
    else: 
        result = 1;

elif(userOption == "Gun" or userOption == "gun"):
    if(computer == "Snake"):
        result = 1;
    
    elif(computer == "Water"):
        result = -1;
    
    else: 
        result = 0;

else:
    print("Please enter a valid option between 'Snake' , 'Water' and 'Gun");


if(result == 1):
    print("You Win..!");
elif(result == 0):
    print("Tie Game...!");
else :
    print("You Loose...!");

