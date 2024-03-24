import random
def randomnumber():
    return random.randrange(1,99)
def guesshint(number,guess):
    if guess > number:
        print("Cold!")
    elif guess == number:
        print("Correct")
    else:
        print("Too Hot!")
def runguess():
    secretnumber = randomnumber()
    while True:
        guess = int(input("Enter Number from 1 to 99: "))
        hint = guesshint(secretnumber,guess)
        if hint == "Correct":
            print("Your guess is correct !!")
            break
        else:
            print(hint)
            
print(runguess())
    
