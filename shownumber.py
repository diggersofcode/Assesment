# Main routine ask if user is ready to process

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]


 #ask if user are ready
ready = input("yes or no: ")

 # if ready program continue
if ready == "yes":
    print("program continue")

# if not ready can try again
elif ready == "no":
    print("Ok, please take your time")

# if enter not valid
else:
    print("Please enter yes or no")

# showing user a number in maori 1-10 if ready
if ready == "yes":
    print (numbers)
    print(maori)
