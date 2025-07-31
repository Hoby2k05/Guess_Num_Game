"""The number guessing game,
where the system chooses a random number on it's own, without letting you know
and you get numebr of attempts depending on the difficulty you choose,
to choose the numebr. It also provides hints, based on how far or close you are
from the chosen number by the system, and you score points based on that as well."""

#.....GIVE IT A TRY YOURSELF.....

import random

palyer_name = input("Enter player name:").strip()
a = int(input("Range starts from: "))
b = int(input("Range ends at: "))

print("Choose difficulty level.\n")
print("1> Easy (10 attempts)\n") #EASY 😀
print("2> Medium (7 attempts)\n") #MEDIUM 😐
print("3> Hard (5 attempts)\n")  #HARD 😨
difficulty = int(input("Enter 1, 2 or 3:").strip())

leaderboard= {} '''Displays a final score        along with the player names.'''

attempts= {1:10,2:7,3:5}.get(difficulty,7)

chosen_one = random.randint(a, b)
guess = None
score = 0
tries = 0



while guess != chosen_one and attempts > 0:
    guess = (input(f"You have {attempts} attempts left. Guess a number between {a} and {b}: ").strip())

    if guess.lower() == "quit":  # ✅ Check for quit command
        confirm = input("Are you sure you want to quit? (yes/no): ").strip().lower()
        if confirm == "yes":
           break  # ✅ Exit the game
        elif confirm == "no":
            continue  # ✅ Go back to guessing

    if not guess.isdigit():  # ✅ Ensure input is a number before converting
        print("Invalid input! Please enter a number or 'quit'.")
        continue  # ✅ Skip this iteration if input isn't a number

    guess = int(guess)


    difference = abs(guess - chosen_one)
    tries +=1

    if guess < a or guess > b:
        print("You are out of range, Try again.")
        continue  # ✅ Skip the rest of the loop without deducting attempts

    if difference == 0:
        print(f"You are absolutely right!🎉. It took {tries} attempts")
        score += 5
        break 
    elif 6<= difference:
        print("You are way off, try again.")
    elif 3<=difference<=5:
        print("You are getting closer!")
        score += 2
    elif 1<=difference<=2:
        print("Too close almost there.")
        score += 5    
    elif guess > chosen_one:
        print("Too high, try again.")    
    elif guess < chosen_one:
        print("Too low, try again.")


    attempts -= 1  # ✅ Now attempts only reduce once per valid guess

    

if attempts == 0 and guess != chosen_one:
    print(f"Out of attempts! The correct number was {chosen_one}. 😢") # OOHH,,,GAME OVER

print(f"Your score is: {score}") # YOUR SCORE 🎉

print("\n 🏆LEADERBOARD🏆") # LEADERBOARD FOR MULTIPALYER MODE....🥇🥈🥉
sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)  # Sort by score
for rank, (name, points) in enumerate(sorted_leaderboard, start=1):
    print(f"{rank}. {name} - {points} points")

