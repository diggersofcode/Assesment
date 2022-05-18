import random
rounds_played = 0
score = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

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
