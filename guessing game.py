import random
rand = random.randint(1, 1000)
while True: 
    print("Guess a number between 1 and 1000")
    guess = int(input("Enter Guess: "))
    if guess == rand:
        cont =  input("You got it right! Go again? y/n ")
        if cont == "y":
            rand = random.randint(1, 1000)
            continue
        else:
            break
    else:
        if guess > rand: 
            print("Too high")
        if guess < rand:
            print("Too low")
        cont = input("Go again? y/n ")
        if cont == "y":
            continue
        else:
            break