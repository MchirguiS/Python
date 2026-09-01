# Made by Shaheen Mchirgui

print(r"""
   ____      _            _       _
  / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __
 | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |__| (_| | | (__| |_| | | (_| | || (_) | |
  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
""")

while True:
    try:
        num = float(input("\nEnter the number: "))
        break
    except ValueError:
        print("Invalid number. Try again:")

print(r"""

        C A L C U L A T O R

        [1]  +     Addition
        [2]  -     Subtraction
        [3]  x     Multiplication
        [4]  /     Division
        [5]  =     Calculate
""")

op = 0

while op < 1 or op > 5:
    try:
        op = int(input("> Choose an operation: "))
        if op < 1 or op > 5:
            print("Choose an operation from 1 to 5:")
    except ValueError:
        print("Invalid input. Enter a number from 1 to 5:")

if op == 5:
    print(f"\nFinal Result: {num}")
    exit()

while True:
    try:
        num2 = float(input("\nEnter the number: "))
        break
    except ValueError:
        print("Invalid number. Try again:")

if op == 1:
    result = num + num2
elif op == 2:
    result = num - num2
elif op == 3:
    result = num * num2
elif op == 4:
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        exit()
    result = num / num2

print(f"\nCurrent Result: {result}")

while op != 5:
    print(r"""

        C A L C U L A T O R

        [1]  +     Addition
        [2]  -     Subtraction
        [3]  x     Multiplication
        [4]  /     Division
        [5]  =     Calculate
""")

    op = 0

    while op < 1 or op > 5:
        try:
            op = int(input("> Choose an operation: "))
            if op < 1 or op > 5:
                print("Choose an operation from 1 to 5:")
        except ValueError:
            print("Invalid input. Enter a number from 1 to 5:")

    if op == 5:
        break

    while True:
        try:
            num2 = float(input("\nEnter the number: "))
            break
        except ValueError:
            print("Invalid number. Try again:")

    if op == 1:
        result += num2
    elif op == 2:
        result -= num2
    elif op == 3:
        result *= num2
    elif op == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            exit()
        result /= num2

    print(f"\nCurrent Result: {result}")

print("\n================================")
print("        FINAL RESULT")
print("================================")
print(f"\n        {result}")
print("\n================================")
