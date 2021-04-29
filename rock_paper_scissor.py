import random as rd
print("Welcome to the Rock Paper Scissors game")
print("\tLet's Play the Game\n")
name = input("Enter your name : ")
user_score = 0
game = 0
while True:
    print("\nChoose between Rock or Paper or Scissor\n")
    user_in = input("Enter Your Choise [R P S] : ")
    choice = ["R","P","S"]
    comp_in = rd.choice(choice)
    print()
    print("You choose {}".format(user_in))
    print("Computer Choose {}".format(comp_in))

    if user_in=="r" or user_in=="R":
        if comp_in=="R":
            print("Tie!\n")
        elif comp_in=="P":
            print("Computer Wins!\n")
        else:
            print(name+" Wins!\n")
            user_score += 1

    elif user_in=="p" or user_in=="P":
        if comp_in=="R":
            print(name+" Wins!\n")
            user_score += 1
        elif comp_in=="P":
            print("Tie!\n")
        else:
            print("Computer Wins!\n")

    elif user_in=="s" or user_in=="S":
        if comp_in=="R":
            print("Computer Wins!\n")
        elif comp_in=="P":
            print(name+" Wins!\n")
            user_score += 1
        else:
            print("Tie!\n")
    else:
        break
    game += 1

print("Total Games : ",game)
print("Your Score : ",user_score)
print("******Thank You******")




            
