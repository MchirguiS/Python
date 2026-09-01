from random import randint

print(r"""
   ____                       _____ _            _   _                 _               
  / ___|_   _  ___  ___ ___  |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |_| | |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \____|\__,_|\___||___/___/   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   


""")

num = randint(1, 100)
print("Number Generated..")

while True:
    try:
        guess = int(input("Guess Number: "))

        if guess < num:
            print("Higher")
        elif guess > num:
            print("Lower")
        else:
            print("Correct!")
            print(f"The number was {num}")
            break

    except ValueError:
        print("Please enter a number.")
