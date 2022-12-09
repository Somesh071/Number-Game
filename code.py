#Guess the random number in given range.
import random

print("WELCOME TO THE GAME!!!!")

print("\nIF YOU WANT TO QUIT THE GAME ENTER 'Quit' ")

a=int(input("\nEnter Lower bound= "))

b=int(input("\nEnter Upper bound= "))

guess=''
while True :
    print()
    score=0
    number=str(random.randint(a,b+1))
    if guess != 'Quit':
        number_of_chances=1
        while number_of_chances<=3:
            guess=input("Enter Your Number: ")

            if guess == 'Quit' :
                break
            else:
                number_of_chances+=1
                if int(guess)<int(number):
                    print("have one more try!!!", "Your guess was too small.")
                elif int(guess)>int(number):
                    print("have one more try!!!", "Your guess was too high.")
                else:
                    score+=1
                    print("Congrat's!!!! Your guess was correct.")
        if guess != 'Quit':
            if score==0:
                print("Better Luck Next Time.")
            else:
                print("Your Winning Score: ",score)
        else:
            break
    else:
        break
