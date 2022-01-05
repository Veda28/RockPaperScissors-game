import random
player_wins=0
computer_wins=0
def userOption():
    user_choice=input("Choose Rock,Paper,Scissors: ")
    if user_choice in ["rock","Rock","r","R"]:
        user_choice= "r"
    elif user_choice in ["paper","Paper","p","P"]:
        user_choice= "p"
    elif user_choice in ["scissors","Scissors","s","S"]:
        user_choice= "s"
    else:
        print("I don't understand. Try Again!!!!")
        userOption()
    return user_choice
def compOption():
    comp_choice=random.randint(1,3)
    if comp_choice == 1:
        comp_choice="r"
    elif comp_choice == 2:
        comp_choice="p"
    else:
        comp_choice="s"
    return comp_choice
while True:
    print("")
    user_choice=userOption()
    comp_choice=compOption()
    if user_choice=="r":
        if comp_choice=="r":
            print("You and computer both chosen rock. You tied.")
        elif comp_choice=="p":
            print("You chose rock and computer chose paper. Computer wins!")
            computer_wins+=1
        elif comp_choice=="s":
            print("You chose rock and computer chose scissors. You win!")
            player_wins+=1
    elif user_choice=="p":
        if comp_choice=="r":
             print("You chose paper and computer chose rock. You win!")
             player_wins+=1
        elif comp_choice=="p":
            print("You and computer both chosen paper. You tied.")
        elif comp_choice=="s":
            print("You chose paper and computer chose scissors. Computer wins!")
            computer_wins+=1
    elif user_choice=="s":
        if comp_choice=="r":
            print("You chose scissors and computer chose rock. Computer wins!")
            computer_wins+=1
        elif comp_choice=="p":
            print("You chose scissors and computer chose paper. You win!")
            player_wins+=1
        elif comp_choice=="s":
            print("You and computer both chosen scissors. You tied.")
    print("Player wins: "+str(player_wins))
    print("Computer wins: "+str(computer_wins))
    user_choice=input("Do you want to play again?(Y/N)")
    if user_choice in ["Yes","yes","Y","y"]:
        pass
    elif user_choice in ["No","no","N","n"]:
        break
    else:
        break
      
        
    
   
   
            
            
            
        
        
