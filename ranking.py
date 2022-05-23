score = ""

while True :

    score = int(input("Score"))
    if score == 1 :
        print("////RANK B////")
    elif score < 1:
        print("////RANK C////")
    else:
        print("////RANK SS////")

