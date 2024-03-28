import random
def randomnumber():
    return random.randrange(1,99)
def guesshint(number,guess):
    if guess > number:
        return "Too hot!"
    elif guess == number:
        return "Correct"
    else:
        return "Too Cold"
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
if __name__ = "__main__":
    runguess()
    
