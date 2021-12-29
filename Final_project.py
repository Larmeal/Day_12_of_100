#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from art import win
from art import lose
import random
print(logo)

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100
""")

# สร้าง list ตัวเลขตั้งแต่ 1 - 100 ขึ้นมาเพื่อทำการสุ่ม
number = []
for i in range(1, 101):
    number.append(i)

random_number = random.choice(number)

# ป้องกันคนที่พิมพ์นอกเนื่องจาก easy และ hard
again = True
while again:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty != "easy" and difficulty !="hard":
        print("You choose only two difficulty between 'easy' or 'hard'")
    if difficulty == "easy" or difficulty =="hard":
        again = False

choose_difficulty = {
    "easy": 10,
    "hard": 5
}

# พลังชีวิต โดยขึ้นอยู่ว่าเลือกเล่น ความยากระดับไหน 
mode_exist = choose_difficulty[difficulty]
mode = mode_exist

# เป็น function สำหรับการบอกพลีงชีวิตว่าเหลืออีกกี่ชีวิต
def play_game():
    again = True
    while again:
        if difficulty == "easy":
            print(f"You have {mode} attempts remaining to guess the number.")
            again = False

        elif difficulty == "hard":
            print(f"You have {mode} attempts remaining to guess the number.")
            again = False

play_game()
guess = int(input("Make a guess: "))

# เป็นขั้นตอนการเล่นเกม ถ้าทายผิดก็จะโดยลบพลังชีวิต
again = True
while again:
    if guess > random_number and mode != 1:
        print("Too high.")
        # ถ้าตอบผิด mode ที่หมายถึงพลังชีวิตจะลดลงเรื่อย ๆ
        mode -= 1
        play_game()
        guess = int(input("Make a guess: "))
        
    elif guess < random_number and mode != 1:
        print("Too low.")
        mode -= 1
        play_game()
        guess= int(input("Make a guess: "))
        
    elif guess == random_number and mode != 1:
        print(f"""
You correct the number, it's {random_number}
{win}

        """)
        again = False
        
    elif mode == 1:
        print(f"""
the number is {random_number}
{lose}

        """)
        again = False

# # my teacher version

# from random import randint

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():

#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()
