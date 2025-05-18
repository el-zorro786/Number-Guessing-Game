import random
x= random.randint(1,50)
print(str(x))
g = 5
y=0
print("This is a Number Guessing Game. You have 5 guesses to guess a number from 1-50")
while x != y:
    print("Guesses left: " + str(g))
    y = int(input("What is your guess: "))
    g=g-1
    ge = -1 * (g-5)
    if x == y:
        print("You win after " + str(ge) + " guesses!")
        break
    if g==0:
        print("You lose :(")
        print("The answer was " + str(x))
        x=y
    if x > y and g!=0:
        print("Too low, try again.")
    if x < y and g!=0:
        print("Too high, try again.")
    
    
        