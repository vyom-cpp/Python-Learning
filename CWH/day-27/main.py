# Define the list of questions, options, and correct answers
questions = [
    {
        "question": "Which of the following is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Lisbon"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
        "answer": "C"
    }
]

# Define the prize money for each question
prize_money = [1000, 5000, 10000]

# Initialize the total prize money
total_prize_money = 0

# Function to play the game
def play_kbc():
    global total_prize_money

    print("Welcome to KBC!")
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Please enter your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("Correct answer!")
            total_prize_money += prize_money[i]
        else:
            print("Incorrect answer. Game over!")
            break

    print(f"\nYou have won a total of Rs. {total_prize_money}")

# Play the game
play_kbc()