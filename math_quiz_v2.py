import random


# To see if user will enter something valid or invalid

def string_checker(Question, valid_ans=None):
    if valid_ans is None:
        valid_ans = ["yes", "no"]

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(Question).lower()

        for item in valid_ans:

            if item == user_response or user_response == item[0]:
                return item

        print(error)

        print()


# The instructions

def instructions():
    print("""

--- Instructions ---

Begin by choosing how many rounds you want to play,

press <enter> for infinite.

Then you will answer one random math question per round.

Answer as many as you can. Good luck!

""")


def int_check(question):
    while True:
        error = "Please enter an integer more than / equal to 1. "

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)
            if response < 1:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


def generate_question():
    math_type = random.choice(['+', '-', '*', '/'])

    if math_type == '+':
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        question1 = f"What is {a} + {b}? "
        answer = a + b

    elif math_type == '-':
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        a, b = max(a, b), min(a, b)  # Make sure answer is not negative
        question1 = f"What is {a} - {b}? "
        answer = a - b

    elif math_type == '*':
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        question1 = f"What is {a} x {b}? "
        answer = a * b

    else:  # Division with whole number result
        b = random.randint(1, 12)
        answer = random.randint(1, 12)
        a = b * answer  # Makes a divisible pair
        question1 = f"What is {a} ÷ {b}? (Whole number only) "

    return question1, answer


# Initialize

mode = "regular"

rounds_played = 0
rounds_correct = 0
rounds_incorrect = 0
quiz_history = []

# Main routine

print("\n✖️➕➖ Math Quiz ➗✖➖➕✖️\n")

want_instructions = string_checker("Do you want to see instructions? ")

if want_instructions == "yes":
    instructions()

num_rounds = int_check("How many rounds would you like to play? Press <enter> for infinite: ")

if num_rounds == "infinite":
    print("You chose infinite mode!")
    mode = "infinite"
    num_rounds = 5

# Game loop
while rounds_played < num_rounds:

    print(f"\n--- Round {rounds_played + 1} ---")

    # Generate and ask one random math question per round

    question, answer = generate_question()

    try:

        user_answer = int(input(question))

        if user_answer == answer:
            # if user gets it correct
            print("Correct! ✅")
            rounds_correct += 1
            feedback = "Correct"
        else:
            # if user gets it wrong
            print(f"Wrong! ❌ The correct answer was {answer}")
            rounds_incorrect += 1
            feedback = "Incorrect"

    except ValueError:

        print(f"Wrong ❌ The correct answer was {answer}")
        rounds_incorrect += 1
        feedback = "Wrong"

    rounds_played += 1

    quiz_history.append(f"Round {rounds_played}: {feedback}")

    if mode == "infinite":
        num_rounds += 1

# Quiz History

if rounds_played > 0:

    print("\n--- Quiz Summary ---")
    print(f"Total Correct ✅: {rounds_correct}")
    print(f"Total Incorrect ❌: {rounds_incorrect}")

    see_history = string_checker("Would you like to see your quiz history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)

    print("\nThanks for playing!")

else:

    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")

