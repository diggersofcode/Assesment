# Get name and age of user
username = input("What is your name?:")
userage = int(input("How old are you?:"))
# variables needed
instruction = "This is a quiz about numbers in Maori, we will show you what number" \
              " 1-10 is in Maori and then you will have to answer an easy question which only a" \
              "sk you what 2 random number is in Maori or you can choose to do more advance one which " \
              "will ask you to say them all in order from 1-10 in Maori."

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
    print (numbers)
    print(maori)
# Choose mode between easy or advance
mode = input("Please choose your mode [easy] or [advance]: ")

# easy mode

if mode == "e   asy":
    print("easy mode ---(you will be asked 2 questions about number in maori)---")

# advance mode

elif mode == "advance":
    print("advance mode ---(write 1-10 in maori in order)---")

    # error
else:
    print("Please enter easy or advance")











