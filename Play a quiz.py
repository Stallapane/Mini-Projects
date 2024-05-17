
print("Hello! Welcome to the Quiz")

play = input("Do you want to play? ")

if play.lower() != 'yes':
    quit()
else:
    print('Lets get started')

score = 0

answer = input("what is the band that never plays music? ")

if answer.lower() == "rubber band":
    print("it's correct")
    score += 1
else:
    print("oops you are wrong :)")


answer = input("Most tensed animal? ")


if answer.lower() == 'kangaroo':
    print("correct")
    score += 1
else:
    print("oh no! Incorrect answer")

answer =  input("who is a short mom? ")


if answer.lower() == 'minimum':
    print("yayy!correct answer")
    score += 1
else:
    print("Incorrect")


answer = input("what kind of shoes spy wears? ")

if answer.lower() == 'sneakers':
    print("correct")
    score += 1
else: 
    print("Better luck next time")

print(f"Your Score is {score}.")




