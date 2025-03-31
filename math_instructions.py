# To see if user will enter something valid or invalid
def string_checker(question, valid_ans=["yes", "no"]):

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
answer as many as you can, once you get one wrong
the game will end.
    """)

# Main routine
print()
print("✖️➕➖Math question✖️➕➖")
print()

# ask user if they want instructions
want_instructions = string_checker("Do you want to see instructions? ")

# if the user want to see instructions then display them
if want_instructions == "yes":
    instructions()

# Int checker user should enter either <enter> or any integer that is more than 0

error = "Please enter an integer more than / equal to 13"
