# Choose mode between easy or advance
while True:
    def difficulty():
        mode = input("Please choose your mode [easy] or [advance]: ")

    # easy mode

        if mode == "easy":
            print("easy mode ---(you will be asked 2 questions about number in maori)---")

    # advance mode

        elif mode == "advance":
            print("advance mode ---(you will be asked 10 questions about number in maori)---")

        # error
        else:
            print("Please enter easy or advance")


    difficulty()
