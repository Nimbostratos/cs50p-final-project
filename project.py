import json

def main():
    questions = load_questions("questions.json")
    print("Welcome to the CS50P Trivia Quiz!")
    print(f"There are {len(questions)} questions.\n")
    results = []
    for q in questions:
        print(q["question"])
        for i, choice in enumerate(q["choices"], 1):
            print(f"{i}. {choice}")
        answer = input("Your answer (enter the number): ").strip()
        correct = ask_question(q, answer)
        if correct:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is: {q['answer']}\n")
        results.append(correct)
    score, percent = calculate_score(results)
    print(f"\nYou scored {score} out of {len(results)} ({percent:.2f}%). Thanks for playing!")

def load_questions(filename):
    with open(filename, "r") as f:
        return json.load(f)

def ask_question(question, user_input):
    ## Return True if user_input is correct answer number, else False.
    try:
        index = int(user_input) - 1
        if 0 <= index < len(question["choices"]):
            selected = question["choices"][index].lower()
            correct = question["answer"].lower()
            return selected == correct
    except ValueError:
        pass
    return False

def calculate_score(results):
    total_correct = sum(results)
    total = len(results)
    percent = (total_correct / total * 100) if total > 0 else 0
    return total_correct, percent

if __name__ == "__main__":
    main()

