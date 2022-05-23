import random


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
