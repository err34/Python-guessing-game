import random
i = 1
max = int(input("Enter max attempts: "))
if max <= 5:
    nMax = 250
elif max < 10:
    nMax = 500
else:
    nMax = 1000
rand = random.randint(1, nMax)
print("Guess a number between 1 and " + str(nMax))
while True: 
    if i > max:
        print("You ran out of tries! The number was " + str(rand))
        cont = input("Go again? y/n ")
        if cont == "y":
            rand = random.randint(1, nMax)
            i = 1
            continue
        else:
            break
    guess = int(input("Enter Guess: "))
    if guess == rand:
        
        cont =  input("You got it right! It took you " + str(i) + " guesses! Go again? y/n ")
        if cont == "y":
            rand = random.randint(1, nMax)
            i = 1
            continue
        else:
            break
    else:
        i+=1
        if guess > rand: 
            print("Too high")
        if guess < rand:
            print("Too low")
        continue