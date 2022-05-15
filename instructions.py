instruction = "This is a quiz about numbers in Maori, we will show you what number" \
              " 1-10 is in Maori and then you will have to answer an easy question which only a" \
              "sk you what 2 random number is in Maori or you can choose to do more advance one which " \
              "will ask you to say them all in order from 1-10 in Maori."
show_instruction = ""
while show_instruction != "x" :


   #ask user if they want to see instructions
    show_instruction = input("Do you want to see instruction?")


   #if yes show instruction
    if show_instruction == "yes" :
        print("show instruction")

   #if no program continues
    elif show_instruction == "no" :
        print("program continues")

   #if error
    else:
        print("Please enter yes or no")

