import random

def roll_dice():
    print("Rolling the dice...")
    print("You rolled a", random.randint(1, 6))

while True:
    choice = input("Roll the dice? (yes/no): ").lower()
    if choice == "yes":
        roll_dice()
    elif choice == "no":
        print("Thanks for playing!")
        break
    else:
        print("Type yes or no only.")
