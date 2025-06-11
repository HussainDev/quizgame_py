question_pool = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
        "answer": "A",
        "answer_text": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Saturn"],
        "answer": "B",
        "answer_text": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Rhino"],
        "answer": "B",
        "answer_text": "Blue Whale"
    },
    {
        "question": "Which language is used to create web pages?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
        "answer": "B",
        "answer_text": "HTML"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C",
        "answer_text": "7"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C",
        "answer_text": "Carbon Dioxide"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Picasso", "B. Michelangelo", "C. Leonardo da Vinci", "D. Van Gogh"],
        "answer": "C",
        "answer_text": "Leonardo da Vinci"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C",
        "answer_text": "8"
    },
    {
        "question": "Which instrument has keys, pedals, and strings?",
        "options": ["A. Guitar", "B. Violin", "C. Piano", "D. Drums"],
        "answer": "C",
        "answer_text": "Piano"
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["A. China", "B. Brazil", "C. UK", "D. Russia"],
        "answer": "B",
        "answer_text": "Brazil"
    },
    {
        "question": "What is H2O commonly known as?",
        "options": ["A. Salt", "B. Water", "C. Oxygen", "D. Hydrogen"],
        "answer": "B",
        "answer_text": "Water"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["A. Earth", "B. Mars", "C. Mercury", "D. Venus"],
        "answer": "C",
        "answer_text": "Mercury"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B",
        "answer_text": "William Shakespeare"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["A. Yuan", "B. Dollar", "C. Yen", "D. Won"],
        "answer": "C",
        "answer_text": "Yen"
    },
    {
        "question": "Which organ is responsible for pumping blood?",
        "options": ["A. Brain", "B. Lungs", "C. Liver", "D. Heart"],
        "answer": "D",
        "answer_text": "Heart"
    },
    {
        "question": "In which sport is the term 'love' used?",
        "options": ["A. Football", "B. Cricket", "C. Tennis", "D. Basketball"],
        "answer": "C",
        "answer_text": "Tennis"
    },
    {
        "question": "Which color is a mix of red and white?",
        "options": ["A. Pink", "B. Purple", "C. Orange", "D. Brown"],
        "answer": "A",
        "answer_text": "Pink"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Go", "B. Gd", "C. Au", "D. Ag"],
        "answer": "C",
        "answer_text": "Au"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["A. 90", "B. 95", "C. 100", "D. 105"],
        "answer": "C",
        "answer_text": "100"
    },
    {
        "question": "Who discovered gravity?",
        "options": ["A. Einstein", "B. Newton", "C. Galileo", "D. Kepler"],
        "answer": "B",
        "answer_text": "Newton"
    }
]


import random

# Use this if you're pasting the question list directly here.
# from questions import question_pool  # If saved in a separate module

# ------------- Main Game Functionality --------------

def run_quiz(question_pool):
    print("🎮 Welcome to the Python Quiz Game!")
    mode = ""
    while mode not in ["easy", "hard"]:
        mode = input("Choose difficulty (easy / hard): ").strip().lower()

    total_qs = 0
    while not (1 <= total_qs <= 10):
        try:
            total_qs = int(input("How many questions do you want? (1 to 10): "))
        except ValueError:
            print("Enter a number between 1 and 10.")

    selected_questions = random.sample(question_pool, total_qs)
    score = 0
    streak = 0
    detailed_results = []

    for index, q in enumerate(selected_questions, start=1):
        print(f"\nQ{index}: {q['question']}")

        if mode == "easy":
            for opt in q["options"]:
                print(opt)
            valid_options = ["A", "B", "C", "D"]
            user_ans = ""
            while user_ans not in valid_options:
                user_ans = input("Your answer (A/B/C/D): ").strip().upper()
                if user_ans not in valid_options:
                    print("❌ Invalid option. Please choose A, B, C, or D.")

            correct = user_ans == q["answer"]

        else:  # hard mode
            user_ans = input("Your answer: ").strip().lower()
            correct = user_ans == q["answer_text"].lower()

        if correct:
            streak += 1
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect! Correct answer: {q['answer_text']}")
            streak = 0

        # Bonus point for every 3 correct in a row
        if streak > 0 and streak % 3 == 0:
            print("🔥 Streak Bonus! +1 point!")
            score += 1

        detailed_results.append({
            "question": q["question"],
            "user_answer": user_ans,
            "correct_answer": q["answer_text"],
            "is_correct": correct
        })

    print("\n🎯 Game Over!")
    print(f"Your final score: {score} / {total_qs + (score // 3)}\n")  # includes streak bonus

    # ------------- Post-game Menu -------------
    while True:
        print("\nWhat would you like to do next?")
        print("1. View detailed scoreboard")
        print("2. Play again")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            print("\n📝 Detailed Scoreboard:")
            for i, res in enumerate(detailed_results, start=1):
                status = "✅" if res["is_correct"] else "❌"
                print(f"\nQ{i}: {res['question']}")
                print(f"Your answer: {res['user_answer']}")
                print(f"Correct answer: {res['correct_answer']}")
                print(f"Result: {status}")
        elif choice == "2":
            run_quiz(question_pool)
            break
        elif choice == "3":
            print("👋 Thanks for playing!")
            break
        else:
            print("Please enter a valid option (1, 2, or 3).")

# Run the game
if __name__ == "__main__":
    run_quiz(question_pool)
