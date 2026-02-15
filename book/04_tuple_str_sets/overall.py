


for i, (question, correct_answer) in enumerate(questions):
    print("Player 1, your turn:")
    print(f"Question {i + 1}: {question}")
    p1_answer = input("Your answer (true/false):\n").lower()
    if p1_answer == correct_answer:
        player1_correct.add(i)
        print("Correct!\n")
    else:
        print("Wrong!\n")


for i, (question, correct_answer) in enumerate(questions):
    print("Player 2, your turn:")
    print(f"Question {i + 1}: {question}")
    p2_answer = input("Your answer (true/false): ").lower()
    if p2_answer == correct_answer:
        player2_correct.add(i)
        print("Correct!\n")
    else:
        print("Wrong!\n")

common_correct = player1_correct.intersection(player2_correct)
unique_p1 = player1_correct.difference(player2_correct)
unique_p2 = player2_correct.difference(player1_correct)


