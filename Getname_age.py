# Get name and age of user
def getname_age():
    through = ""
    while through != "x":

        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        print(f"****You are {age} year old and your name is {name}****")
        through = "x"


getname_age()


