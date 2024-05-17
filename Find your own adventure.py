
name = input("Hello :) enter you name: ")

print("Hi", name , "welcome to the adventure")

answer =  input("you are on a dirt road. do you want to go left or right? ").lower()

if answer == "left":
    answer = input("You entered water world do you want to go swimming or walk around enter swim to go swimming or enter walk to walk around").lower()
    if answer == 'swim':
        print("you went swimming and turned into a mermaid")
    elif answer == 'walk':
        print("you walked a lot charge your battery")
elif answer == "right":
    answer = input("you entered a magic land do you want to explore or go back? type explore to goahead or type back to walk away: ").lower()
    if answer == "back":
        print("you walked away, you loose")
    elif answer == 'explore':
            answer = input("There is a stranger walking around do you want to ask help to navigate? yes/no: ").lower()
            if answer == 'no':
                print("You walked arund and lost the way")
            elif answer == 'yes':
                    print("you got the map and found the gold. congrats")
            else:
                print("enter valid answer")
    else:
        print(" enter valid answer")
else:
    print("Not a valid answer, You lost!")





