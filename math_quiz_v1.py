import random


# To see if user will enter something valid or invalid
def string_checker(question, valid_ans=None):
    if valid_ans is None:
        valid_ans = ["yes", "no"]
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Check users response if it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        # print error if user does enter something invalid
        print(error)
        print()


# The instructions
def instructions():
    print("""
---Instructions---

begin by choosing how many rounds you want to play,
press <enter> for infinite.
then you will answer random math questions,
answer as many as you can.
    """)


def int_check(question):
    while True:
        error = "Please enter an integer more than / equal to 1. "

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def quiz_result(correct, incorrect):

    # if user gets questions right
    if user_answer == answer:
        quiz_result = "correct"

    elif user_answer == answer2:
        quiz_result = "correct"
    elif user_answer == answer3:
        quiz_result = "correct"
    elif user_answer == answer4:
        quiz_result = "correct"
    # if user gets it wrong
    else:
        quiz_result = "incorrect"

    return quiz_result



# Initialize
mode = "regular"

rounds_played = 0
rounds_correct = 0
rounds_incorrect = 0

quiz_history = []

# Main routine
print()
print("✖️➕➖Math question✖➖➕✖️")
print()

# ask user if they want instructions
want_instructions = string_checker("Do you want to see instructions? ")

# if the user want to see instructions then display them
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play? Please press <enter> for infinite: ")

if num_rounds == "infinite":
    print("You chose infinite!!")
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # rounds headings
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (infinite mode)"
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)

    # generating the number limit
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3, num4 = sorted((random.randint(1, 100), random.randint(1, 100)), reverse=True)
    num5 = random.randint(1, 20)
    num6 = random.randint(1, 20)
    num7, num8 = sorted((random.randint(1, 120), random.randint(1, 15)), reverse=True)

    # Math question

    print()

    # Addition
    print(f"What is {num1} + {num2} = ?")
    user_answer = int_check("")
    answer = num1 + num2
    if user_answer == answer:
        print("Correct!!✅✅")
        rounds_correct += 1
    else:
        print(f"Wrong!!❌❌ "
              f"It was {answer}")
        rounds_incorrect += 1

    print()

    # Subtraction
    print(f"What is {num3} - {num4} = ?")
    user_answer = int_check("")
    answer2 = num3 - num4
    # if user gets it correct or wrong
    if user_answer == answer2:
        print("Correct!!✅✅")
        rounds_correct += 1
    else:
        print(f"Wrong!!❌❌ "
              f"It was {answer2}")
        rounds_incorrect += 1

    print()

    # Multiplication
    print(f"What is {num5} x {num6} = ?")
    user_answer = int_check("")
    answer3 = num5 * num6
    # if user gets it correct or wrong
    if user_answer == answer3:
        print("Correct!!✅✅")
        rounds_correct += 1
    else:
        print(f"Wrong!!❌❌ "
              f"It was {answer3}")
        rounds_incorrect += 1

    print()

    # Division
    print(f"What is {num7} ÷ {num8} = ?"
          f"Please keep the answer a whole number")
    user_answer = int_check("")
    answer4 = num7 // num8
    # if user get it correct or wrong
    if user_answer == answer4:
        print("Correct!!✅✅")
        rounds_correct + 1
    else:
        print(f"Wrong!!❌❌ "
              f"It was {answer4}")
        rounds_incorrect + 1

    rounds_played += 1

    result = quiz_result(rounds_correct, rounds_incorrect)

    if result == "correct":
        rounds_correct += 1
        feedback = "You got it correct"
    if result == "incorrect":
        rounds_incorrect += 1
        feedback = "Incorrect"

    rounds_feedback = f"Total {rounds_correct}✅ | Total {rounds_incorrect}❌"
    history_item = f"Round: {rounds_played} | {rounds_feedback}"

    print(rounds_feedback)
    quiz_history.append(history_item)

    # if user chose infinite
    if mode == "infinite":
        num_rounds += 1

    print()

if rounds_played > 0:
        # Rounds end here
    # Quiz history
    see_history = string_checker("Do you want to see your quiz history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)

    print()
    print("Thanks for playing.")

else:
    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")

