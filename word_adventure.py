name = input("Type your name: ").capitalize()
print("Hello", name + " ! Its time to choose your adventure!! ")
print("Note: The options in the bracket are the only acceptable options").upper()

answer = input("You're on a dirt road and have reached crossed roads, what way do you go?"
               " (left/ right/ straight): ").lower()
if answer == "left":
    answer = input( "You come to a river. Do you sit at the bank to think of your next move or \
     try to swim across? (sit/swim): ").lower()
    if answer == "sit":
        print("A man with a boat saw you , he gave you some food and gave you the right directions out of town. ")
        print("You are safe! You win!")
    elif answer == "swim":
        print("You were devoured by an alligator")
        print("You lose")
        print("Thanks for trying ", name + " .")
    else:
        print("Not an option. You lose")


elif answer == "right":
    answer = input("You met a tired stranger. Ask for directions and help with load or pass by? (help/pass): ").lower()
    if answer == "help":
        print("The stranger took you home and fed you. Gave you a piece of gold to appreciate you and helped you \
         out of the village ")
        print("You are safe and richer! You win!")

    elif answer == "pass":
        print("You got lost and died thirsty and famished")
        print("You lose")
        print("Thanks for trying ", name + " .")

    else:
        print("Not an option. You lose")

elif answer == "straight":
    print("You're in luck! You chose the right path!!")

else:
    print("Not an option. You lose")
