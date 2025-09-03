import random

check = True
counter = 0
guessed_num = 0

while(check):
    num1 = input("Enter the first Number.")
    num2 = input("Enter the Second Number.")
    try:
        num1 = int(num1)
        num2 = int(num2)
        if num2 > num1:
            check = False
        else:
            print("Please enter a valid Range.")
    except:
        print("Either of the two inputs is not numeric.")
        print("Please enter numbers !")
        check = True

mystery_num = random.randint(num1,num2)

while(guessed_num != mystery_num):
    guessed_num = int(input("Guess the Number :) "))
    counter += 1
    if guessed_num > mystery_num:
        print("Number is Too High")
    elif guessed_num < mystery_num:
        print("Number is Too Low")

if guessed_num == mystery_num:
    print("You guessed it right !")
    print(f"It took you {counter} tries")