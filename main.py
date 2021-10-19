import random
randNumber=random.randint(1,101)
guess=0
userGuess=None
while(userGuess!=randNumber):
    userGuess=int(input("Enter your guess: "))
    if(userGuess==randNumber):
        print(f"Your guess is correct in {guess} guess!")
    else:
         if userGuess>randNumber:
            print("Enter Small number")
            guess=guess+1
         if userGuess<randNumber:
            print("Enter big NUmber")
            guess=guess+1
