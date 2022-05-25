import random
# Get name and age of user

username = input("What is your name?:")
userage = int(input("How old are you?:"))
# variables needed
instruction = "This is a quiz about numbers in Maori, we will show you what number" \
              " 1-10 is in Maori and then you will have to answer an easy question which only a" \
              "sk you what 2 random number is in Maori or you can choose to do more advance one which " \
              "will ask you to answer 10 question of number in maori. After game is finish, we will tell you what your" \
              "score is and rank you got. "

# function for easy mode


def easy():
    rounds_played = 0
    score = 0
    while rounds_played < 2:
        question = random.choice(numbers)
        attempt = input(f"What is maori word for {question}: ")
        rounds_played += 1
    # Using the index position of the question in one list to find the corresponding
    # index position of the answer
        answer_index = numbers.index(question)
        answer = maori[answer_index]

    # Compare the attempt to see if it matches the correct answer
        if attempt == answer:
            print("##### CORRECT! ####\n")
            score += 1
        else:
            print("XXXX INCORRECT! XXXX\n")
    print(f"***you got {score} points!***")
    if score == 1:
        print("////RANK B////")
    elif score < 1:
        print("////RANK C////")
    else:
        print("////RANK SS////")

# function for advance mode


def advance():
    score = 0
    rounds_played = 0
    while rounds_played < 10:
        question = random.choice(numbers)
        attempt = input(f"What is maori word for {question}: ")
        rounds_played += 1
    # Using the index position of the question in one list to find the corresponding
    # index position of the answer
        answer_index = numbers.index(question)
        answer = maori[answer_index]

    # Compare the attempt to see if it matches the correct answer
        if attempt == answer:
            print("##### CORRECT! ####\n")
            score += 1
        else:
            print("XXXX INCORRECT! XXXX\n")
    print(f"***you got {score} points!***")
    if score < 3:
        print("////RANK C////")
    elif score < 5:
        print("////RANK B////")
    elif score == 10:
        print("////RANK SS////")
    elif score >= 5:
        print("////RANK A////")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

# Print instructions and your information
# check if age entered  is int value
if type(userage) == int:
    print(f"Hello {username} you are currently {userage} year old")
    print(instruction)
    print("----------------------Are you ready?--------------------------------")
else:
    print("Please enter your name or age")


# Main routine ask if user is ready to process
ready = input("yes or no: ")
if ready == "yes":
    print("program continue")
elif ready == "no":
    print("Ok, please take your time")
else:
    print("Please enter yes or no")

# showing user a number in maori 1-10
if ready == "yes":
    print(numbers)
    print(maori)
# Choose mode between easy or advance
mode = input("Please choose your mode [easy] or [advance]: ")

# easy mode

if mode == "easy":

    print("*****easy mode begin*****")
    print("/////Have fun!/////")
    easy()

elif mode == "advance":
    print("*****advance mode, BEGIN!!*****")
    print("/////Good luck and try your best!/////")
    advance()
    # error
else:
    print("Please enter easy or advance")

print("///THANKS FOR PLAYING///")










